"""João, Papo-De-Pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas."""

maxWeight = 50.0
excessPrice = 4.0

def calculateFee(weight):
    if(weight <= maxWeight):
        return 0
    else:
        return (weight - maxWeight) * excessPrice


def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

weight = readNumber("Digite o peso dos peixes: ")
fee = calculateFee(weight)
if(fee == 0):
    print("Não houve excesso de peso. Nenhuma multa é necessaria.")
else:
    print(f"O excesso de peso foi de {'{:.2f}'.format(weight - maxWeight)} quilos. A multa é de R$ {'{:.2f}'.format(fee)}.")


