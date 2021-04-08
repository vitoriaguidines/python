N = int(input())
t = 1
for i in range(N):
    cartas = list(map(int, input().split()))
    cartas.sort()

    sequencia = True
    quadra = False
    full_house = False
    trinca = False
    dois_pares = False
    par = False

    x = min(cartas)
    for j in range(len(cartas)-1):
        if cartas[j] != cartas[j+1]-1:
            sequencia = False
        if cartas.count(cartas[j]) == 4:
            x = cartas[j]
            quadra = True
            break
        if cartas.count(cartas[j]) == 3 and par == False:
            trinca = True
            x = cartas[j]
            for k in range(3):
                cartas[j+k] = max(cartas) + 1
        if cartas.count(cartas[j]) == 3 and par == True:
            full_house = True
            par = False
            x = cartas[j]
            cartas[j] = max(cartas) + 1
            break
        if cartas.count(cartas[j]) == 2 and trinca == False and par == False:
            par = True
            x = cartas[j]
            cartas[j] = max(cartas) + 1
        if cartas.count(cartas[j]) == 2 and trinca == False and par == True:
            par = False
            dois_pares = True
            if x < cartas[j]:
                y = x
                x = cartas[j]
            else:
                y = cartas[j]
            cartas[j] = max(cartas) + 1
            break
        if cartas.count(cartas[j]) == 2 and trinca == True:
            full_house = True
            trinca = False
            cartas[j] = max(cartas) + 1
            break

    resposta = 0

    if sequencia:
        resposta = x+200

    if quadra:
        resposta = x+180

    if full_house:
        resposta = x+160

    if trinca:
        resposta = x+140

    if dois_pares:
        resposta = 3x +2y +20

    if par:
        resposta = x


    print("Teste", t)
    t += 1
    print(resposta)
    print()