"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte formula: (72.7 * altura) - 58"""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

height = readNumber("Digite a altura (ex.: 1.68): ")
weight = "{:.2f}".format(( 72.7 * height) - 58)
print(f"O peso ideal é {weight} quilos.")
