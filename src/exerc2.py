"""Faça um programa que peça um numero e entao mostre a mensagem 'O numero informado foi [NUMERO]'."""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

number = readNumber("Digite um numero: ")
print(f"O numero informado foi {number}.")
