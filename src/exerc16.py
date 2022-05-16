"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

MTS_PER_LITER = 3
LITER_PER_BOTTLE = 18
PRICE_PER_BOTTLE = 80

#criando metodo de arredondamento para nao usar bibliotecas
def roundUp(value):
    return int(value + 0.99)

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

mts = readNumber("Digite a area em metros quadrados para ser pintada: ")
lts = mts / MTS_PER_LITER
bottles = roundUp(lts / LITER_PER_BOTTLE)
totalValue = bottles * PRICE_PER_BOTTLE

print(f"Serão necessarios {bottles} latas de tinta dando um total de {'{:.2f}'.format(totalValue)} reais.")

