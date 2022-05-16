"""Faça um programa que peça as 4 notas bimestrais e mostre a media"""

def readNumbers(count):

    print(f"Digite {count} notas separadas por espaço.")
    numbers = input().split(" ")
    while numbers.count('') > 0: 
        numbers.remove("")
    if len(numbers) > count:
        print(f"Você digitou mais do que {count} notas.")
        print(f"considerando apenas os primeiros {count} notas.")
        numbers = numbers[:count]
    if(len(numbers) < count):
        print(f"Você digitou menos do que {count} notas.")
        return readNumbers(count)
    try:
        for i in range(len(numbers)):
            numbers[i] = float(numbers[i])
        return numbers
    except:
        print("Entrada invalida!")
        return readNumbers(count)

numbers = readNumbers(4)
media = sum(numbers) / len(numbers)
print(f"A média é {media}.")
