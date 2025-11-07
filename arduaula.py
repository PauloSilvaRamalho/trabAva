# python -m venv .\NOME DO ARQUIVO\
# cd .\NOME DO ARQUIVO\ 
# .\Scripts\activate
#  pip install -r .\requirements.txt

import serial
import time
import os

junt = ''
porta ="COM5"
baudrate = 9600
arduino = serial.Serial(porta,baudrate,timeout=1)
time.sleep(2)

def titulo():
    print("""
████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████████░░▄▀░░█░░▄▀░░█████████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████████████
""")
    print("\n")


def escrita(comando):
    while True:
        if arduino.in_waiting>0:
            morseFront = arduino.readline().decode().strip()
            print(morseFront)
            if comando == True:
                break

# def main():
#     os.system("cls")
#     titulo()
#     while True:
#         comando = input("pressione enter para mandar o codigo")
#         if comando == "enter":
#             if arduino.in_waiting>0:
#                 resposta = arduino.readline().decode().strip()
#                 print(resposta)       
                    
def main(junt = ''):
    os.system("cls")
    titulo()
    while True:
        # comando = input("pressione enter para mandar o codigo")
        # if comando == "enter":
            if arduino.in_waiting>0:
                resposta = arduino.readline().decode().strip()
                if resposta == '':
                    resposta = ' '
                junt = junt + resposta
                print(junt)                     
                
                
if __name__ == "__main__":
    main()    
