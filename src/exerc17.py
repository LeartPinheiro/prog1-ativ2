"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
 Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 comprar apenas latas de 18 litros;
 comprar apenas galões de 3,6 litros;
 misturar latas e galões, de forma que o desperdício de tinta seja menor. 
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

BIG_BOTTLE = {
        "liters": 18,
        "price": 80.0,
    }

SMALL_BOTTLE = {
        "liters": 3.6,
        "price": 25.0,
    }

BOTTLES = [BIG_BOTTLE, SMALL_BOTTLE]

MARGIN_MULTIPLIER = 1.1
MTS_PER_LITER = 6

def roundUp(value):
    return int(value + 0.99)

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)
 
def calculateMultiplesBottles(lts, bottles):
    for bottle in bottles:
       if lts % bottle["liters"] == 0:
              bottle["quant"] += lts / bottle["liters"]
              return bottles   
    for (index, bottle) in enumerate(bottles):
        if index == len(bottles) - 1:
            bestIndex = 0
            for (i, b) in enumerate(bottles):
                bestRemaining = roundUp(lts / bottles[bestIndex]["liters"]) * bottles[bestIndex]["liters"] - lts
                actualRemaining = roundUp(lts / b["liters"]) * b["liters"] - lts
                if actualRemaining < bestRemaining:
                    bestIndex = i
            bottles[bestIndex]['quant'] += roundUp(lts / bottles[bestIndex]["liters"])
            return bottles
        elif lts >= bottle['liters']:
            quant = int(lts / bottle['liters'])
            lts -= bottle['liters'] * quant
            bottles[index]['quant'] += quant
            return calculateMultiplesBottles(lts, bottles)


def calculateBottles(lts, bottles):
    if(len(bottles) == 1):
        bottle = bottles[0].copy()
        bottle["quant"] = roundUp(lts / bottle["liters"])
        return [bottle]
    else:
        tempBottles = []
        for bottle in bottles:
            b = bottle.copy()
            b["quant"] = 0
            tempBottles.append(b)
        tempBottles.sort(key=lambda x: -x["liters"])
        return calculateMultiplesBottles(lts, tempBottles)
        
def printBottlesTable(bottles):
    print("{:>10} {:>10} {:>10} {:>10}".format("Litros", "Preço.unit", "Latas", "Preço"))
    for bottle in bottles:
        if bottle["quant"] > 0:
            print("{:>10} {:>10} {:>10} {:>10}".format(bottle["liters"], bottle["price"], bottle["quant"], bottle["quant"] * bottle["price"]))
        
mts = readNumber("Digite a area em metros quadrados para ser pintada: ")
lts = mts / MTS_PER_LITER * MARGIN_MULTIPLIER
onlyBig = calculateBottles(lts, [BIG_BOTTLE])[0]
onlySmall = calculateBottles(lts, [SMALL_BOTTLE])[0]
mixBottles = calculateBottles(lts, BOTTLES)

print("\n")
total = onlyBig['quant'] * onlyBig['price']
print(f"Se optar por comprar apenas galão(s) de 18 litros devera comprar {onlyBig['quant']} galão(s) no valor total de {total} reais." )
total = onlySmall['quant'] * onlySmall['price']
print(f"Se optar por comprar apenas lata(s) de 3.6 litros devera comprar {onlySmall['quant']} lata(s) no valor total de {total} reais." )
print("\n")

total = 0
for bottle in mixBottles:
    total += bottle['quant'] * bottle['price']
print("Se optar pos misturar latas e galões, devera comprar:")
printBottlesTable(mixBottles)
print(f"O valor total será de {total} reais.")













            
        






 