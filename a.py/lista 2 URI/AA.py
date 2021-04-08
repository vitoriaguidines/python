import random

dia1 = int(input("Insira o primeiro dia = "))
mes1 = int(input("Insira o primeiro mês = "))
ano1 = int(input("Insira o primeiro ano = "))
dia2 = int(input("Insira o segundo dia = "))
mes2 = int(input("Insira o segundo mês = "))
ano2 = int(input("Insira o segundo ano = "))

if(ano2 > ano1):
    dianovo = random.randint(1, 31)
    mesnovo = random.randint(1, 12)
    anonovo = random.randint(ano1, ano2)
elif(ano1 > ano2):
    dianovo = random.randint(1, 31)
    mesnovo = random.randint(1, 12)
    anonovo = random.randint(ano2, ano1)
else:
    anonovo = ano1
    if (mes2 > mes1):
        dianovo = random.randint(1, 31)
        mesnovo = random.randint(mes1 + 1, mes2 - 1)
    elif (mes1 > mes2):
        dianovo = random.randint(1, 31)
        mesnovo = random.randint(mes2 + 1, mes1 - 1)
    else:
        mesnovo = mes1
        if (dia2 > dia1):
            dianovo = random.randint(dia1 + 1, dia2 - 1)
        elif (dia1 > dia2):
            dianovo = random.randint(dia2 + 1, dia1 - 1)
        else:
            dianovo = dia1

if(dia2 == dia1 and mes2 == mes1 and ano2 == ano1):
    print("As datas são iguais.")
else:
    print(dianovo, mesnovo, anonovo)