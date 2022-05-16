"""Faça um programa que peça dois numeros imprima a soma."""

def readNumbers(count):

    print(f"Digite {count} numeros separados por espaço.")
    numbers = input().split(" ")
    while numbers.count('') > 0: 
        numbers.remove("")
    if len(numbers) > count:
        print(f"Você digitou mais do que {count} numeros.")
        print(f"considerando apenas os primeiros {count} numeros.")
        numbers = numbers[:count]
    if(len(numbers) < count):
        print(f"Você digitou menos do que {count} numeros.")
        return readNumbers(count)
    try:
        for i in range(len(numbers)):
            numbers[i] = float(numbers[i])
        return numbers
    except:
        print("Entrada invalida!")
        return readNumbers(count)

numbers = readNumbers(2)
print(f"A soma dos numeros é {numbers[0] + numbers[1]}.")
