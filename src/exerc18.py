"""Faça um programa que peça o tamanho de um arquivo para download (em mb) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

file = readNumber("Digite o tamanho do arquivo em MB: ")
speed = readNumber("Digite a velocidade do link em Mbps: ")
time =   file * 8 / speed / 60
minutos = int(time)
segundos = int((time - minutos) * 60)
print(f"O tempo aproximado de download do arquivo é de {minutos} minutos e {segundos} segundos.")