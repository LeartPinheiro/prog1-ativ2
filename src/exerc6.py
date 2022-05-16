"""faça um programa que peça o raio de um circulo,calcule e mostre sua area."""

PI = 3.14159

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

r = readNumber("Digite o raio do circulo: ")
area = PI * r * r
print(f"A area do circulo é {area}.")
