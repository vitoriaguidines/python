N = int(input())
teste = 1
while(N != 0):
    nome1 = input()
    nome2 = input()
    print("Teste", teste)
    for i in range(N):
        A, B = map(int, input().split())
        if((A + B) % 2 == 0):
            print(nome1)
        else:
            print(nome2)
    print("")
    teste += 1
    N = int(input())