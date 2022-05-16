"""Faça um programa que peça 2 numeros inteiros e um numero real. Calcule e mostre:
* O produto do dobro do primeiro com metade do segundo.
* A soma do triplo do primeiro com o terceiro.
* O terceiro elevado ao cubo."""

def readNumber(message,onlyInt=False):
    try:
        if onlyInt:
            return int(input(message))
        else:
            return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message,onlyInt)

int1 = readNumber("Digite o primeiro inteiro: ",onlyInt=True)
int2 = readNumber("Digite o segundo inteiro: ",onlyInt=True)
real = readNumber("Digite um numero real: ")

print(f"O produto do dobro do primeiro com metade do segundo é {(int1 * 2) * (int2 / 2)}.")
print(f"A soma do triplo do primeiro com o terceiro é {(int1 * 3) + real}.")
print(f"O terceiro elevado ao cubo é {real ** 3}.")
