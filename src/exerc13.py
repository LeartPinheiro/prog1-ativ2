"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
* Para homens: (72.7*h) - 58
* Para mulheres: (62.1*h) - 44.7"""

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

def readGender():
    print("Digite 'm' para homem ou 'f' para mulher: ")
    gender = input()
    if(gender != 'm' and gender != 'f'):
        print("entrada invalida!")
        return readGender()
    else:
        return gender

height = readNumber("Digite a altura (ex.: 1.68): ")
gender = readGender()
msg = ''
if(gender == 'm'):
    weight = "{:.2f}".format((72.7*height) - 58)
    msg = f"Seu peso ideal sendo homem é: {weight} quilos."
else:
    weight = "{:.2f}".format((62.1*height) - 44.7) 
    msg = f"Seu peso ideal sendo mulher é: {weight} quilos."

print(msg)
