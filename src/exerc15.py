"""Faça um programa que pergunte o quanto você gaha por hora e o numero de horas trabalhadas no mes.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
 faça um programa que nos dê:
 a. salário bruto.
 b. quanto pagou ao INSS.
 c. quanto pagou ao sindicato.
 d. o salário líquido.
 e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
 + Salário Bruto : R$
 - IR (11%) : R$
 - INSS (8%) : R$
 - Sindicato ( 5%) : R$
 = Salário Liquido : R$"""

IR = 0.11
INSS = 0.08
SINDICATO = 0.05

DISPLAY_FORMULA = "{:7.2f}"

def printPayment(value):
    ir = value * IR
    inss = value * INSS
    sindicato = value * SINDICATO
    liquid = value - ir - inss - sindicato
    print("+ Salário Bruto :".ljust(25)," R$ ", DISPLAY_FORMULA.format(value))
    print(f"- IR ({IR * 100}%) :".ljust(25)," R$ ", DISPLAY_FORMULA.format(ir))
    print(f"- INSS ({INSS * 100}%) :".ljust(25)," R$ ", DISPLAY_FORMULA.format(inss))
    print(f"- Sindicato ({SINDICATO * 100}%) :".ljust(25)," R$ ", DISPLAY_FORMULA.format(sindicato))
    print("= Salário Liquido :".ljust(25)," R$ ", DISPLAY_FORMULA.format(liquid))

def readNumber(message):
    try:
        return float(input(message))
    except:
        print("Entrada invalida!")
        return readNumber(message)

gainPerHour = readNumber("Digite o quanto você ganha por hora: ")
workedHours = readNumber("Digite quantas horas você trabalhou nesse mês: ")
printPayment(gainPerHour * workedHours)


