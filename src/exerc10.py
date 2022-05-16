"Faça um programa que peça a temperatura em graus celsius, transforme e mostre a temperatura em graus fahrenheit."

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

cel = readNumber("Digite a temperatura em Celsius: ")
fah = (cel * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é {fah}.")
