N = int(input())

for i in range(N):
    palavra = input().split()
    resposta = ""
    for j in range(len(palavra)):
        resposta += palavra[j][0]
    print(resposta)