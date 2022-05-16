"""Faça um programa que converta metros em cm"""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

meters = readNumber("Digite a quantidade de metros: ")
print(f"{meters} metros são {meters * 100} centimetros.")
