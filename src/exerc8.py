"""Faça um progama que pergunte quanto você ganha por hora e o numeros de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

gainPerHour = readNumber("Digite o quanto você ganha por hora: ")
workedHours = readNumber("Digite quantas horas você trabalhou nesse mês: ")

print(f"Você deve ganhar {'{:.2f}'.format(gainPerHour * workedHours)} reais nesse mês.")
