#Bibliotecas
import os
from dotenv import load_dotenv
from google import genai
import serial
import time

#Configuração de Arduino
# porta ="COM3"
# baudrate = 9600
# arduino = serial.Serial(porta,baudrate,timeout=1)
# time.sleep(2)


#Configuração de Modelo
MODELO = "gemini-2.5-flash-lite"

# pip install gTTS pygame


def titulo():
    print("""
████████████████████████████
█─▄▄▄─█████▄─▄███████▄─██─▄█
█─███▀█░░███─██▀█░░███─██─██
▀▄▄▄▄▄▀▄▄▀▀▄▄▄▄▄▀▄▄▀▀▀▄▄▄▄▀▀ """)
    print("\n")

def perguntar_modelo(cliente, MODELO, prompt):
    resposta = cliente.models.generate_content(model=MODELO,contents=prompt)
    texto = getattr(resposta, "text","") or ""
    return texto

# def falar(texto):
#     arq = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
#     arq.close()
#     gTTS(texto,lang = "pt-br").save(arq.name)
#     pygame.mixer.init()
#     pygame.mixer.music.load(arq.name)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         time.sleep(0.1)
#     pygame.mixer.quit()
#      os.remove(arq.name)    

def carregar_chave():
    load_dotenv()
    chave = (os.getenv("GOOGLE_APY_KEY"))
    if not chave:
        print("Faltando a chave dentro do arquivo .env")
        raise SystemExit(1)
    return chave

def montar_prompt(sistema, historico, pergunta):
    partes = [sistema]
    for turno in historico:
        if turno["papel"] == "Aluno":
            quem = "Aluno"
        else: 
            quem = "C.L.U"
        partes.append(f"{quem}: {turno["texto"]}")
    partes.append(f"Aluno: {pergunta}")
    partes.append("C.L.U")
    return "\n".join(partes)



def main():
    os.system("cls")
    titulo()
    chave = carregar_chave()
    cliente = genai.Client(api_key=chave)
    # criar Historico
    historico = []
    print("C.L.U => Olá, eu sou a inteligencia artificial da disciplina IOT")
    while True:
        pergunta = input("Você => ")
        if not pergunta:
            continue
        #Comandos
        if pergunta.lower() == "sair":
            break

        # if pergunta.lower() == "ligar led":
        #      arduino.write('1'.encode())
        #      while True:
        #         if arduino.in_waiting>0:
        #             resposta = arduino.readline().decode().strip()
        #             print(resposta)
        #             break
        #      continue 

        # if pergunta.lower() == "desligar led":
        #      #arduino.write('0'.encode())
        #      while True:
                #  if arduino.in_waiting>0:
                #      resposta = arduino.readline().decode().strip()
                #      print(resposta)
                #      break
            #  continue 

        # if pergunta.lower() == "medir distancia":
        #      arduino.write('2'.encode())
        #      while True:
        #          if arduino.in_waiting>0:
        #              resposta = arduino.readline().decode().strip()
        #              print(resposta)
        #              break
        #      continue

        # if pergunta.lower() == "quero cafe":
        #      arduino.write('3'.encode())
        #      while True:
        #          if arduino.in_waiting>0:
        #              resposta = arduino.readline().decode().strip()
        #              print(resposta)
        #              resposta = arduino.readline().decode().strip()
        #              print(resposta)
        #              break
        #      continue                                          


        sistema = "Você é um assistente. Responda em portugues do Brasil, claro, direto, e no máximo 2-3 frases"
        prompt = montar_prompt(sistema, historico, pergunta)        
        
        #Chamar modelo
        resposta = perguntar_modelo(cliente,MODELO,prompt)

        historico.append({"papel":"aluno", "texto": pergunta})
        historico.append({"papel":"C.L.U", "texto": resposta})

        print(f"C.L.U => {resposta}")

        #falar(resposta)

if __name__ == "__main__":
    main()