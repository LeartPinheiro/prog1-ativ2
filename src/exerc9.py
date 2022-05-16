"""Faça um programa que peça a tempetura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F - 32) / 9)."""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

fah = readNumber("Digite a temperatura em Fahrenheit: ")
cel = 5 * ((fah - 32) / 9)
print(f"A tempetura em Celsius é {cel}.")
