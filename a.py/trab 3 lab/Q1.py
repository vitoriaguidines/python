import random
m, n = map(int, input().split())
matrix = []

for i in range(m):
    lista = []
    for j in range(n):
        if(i == j):
            lista.append(i)
        elif(i < j):
            lista.append(round(random.uniform(5, 9.99), 2))
        elif(j < i):
            lista.append(random.randint(-10, -5))
    matrix.append(lista)

for row in matrix:
    for col in row:
        print(f'[{col:^5}]', end='')
    print()