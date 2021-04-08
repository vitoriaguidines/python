t = 0
n = int(input())
while n != 0:
    t += 1
    print("Teste %d" % t)

    contadores = [[0] * 10 for i in range(6)]

    for i in range(n):
        s = input().split()
        digitos = list(map(int, s[0:10]))
        letras = s[10:16]
        
        for ind in range(6):
            letra = letras[ind]

            d1, d2 = -1, -1
            if letra == 'A':
                d1, d2 = digitos[0], digitos[1]
            elif letra == 'B':
                d1, d2 = digitos[2], digitos[3]
            elif letra == 'C':
                d1, d2 = digitos[4], digitos[5]
            elif letra == 'D':
                d1, d2 = digitos[6], digitos[7]
            else:
                d1, d2 = digitos[8], digitos[9]

            contadores[ind][d1] += 1
            contadores[ind][d2] += 1

    for ind in range(6):
        frequencias = contadores[ind]

        maior_f = -1
        maior_d = None
        for d in range(10):
            if maior_f < frequencias[d]:
                maior_f = frequencias[d]
                maior_d = d
        print(maior_d, end=" ")

    print("\n")
    n = int(input())