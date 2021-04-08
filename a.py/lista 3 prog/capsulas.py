N = list(map(int, input().split()))

capsulas = N[0]
moedas = N[1]

ciclos = list(map(int, input().split()))

inicio = 1
fim = 10**8

while inicio < fim:
    meio = int((inicio+fim)/2)
    total_meio = 0
    for i in range(len(ciclos)):
        total_meio += meio//ciclos[i]
    if total_meio >= moedas:
        fim = meio
    else:
        inicio = meio+1