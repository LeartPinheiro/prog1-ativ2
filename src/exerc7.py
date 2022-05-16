"""Faça um programa que calcule a area de um quadrado, em seguida mostre o dobro da area para o usuario."""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

lat = readNumber("Digite a largura do quadrado: ")
print(f"O dobro da area do quadrado é {lat * lat * 2}.")
