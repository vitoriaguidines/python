N = input().split()

t = 1
while N != ["0", "0"]:
    resp = ""
    voos = [0] * int(N[0])
    aer = []
    for i in range(int(N[1])):
        M = input().split()
        voos[int(M[0])-1] += 1
        voos[int(M[1])-1] += 1

    maior = max(voos)

    for i in range(len(voos)):
        if voos[i] == maior:
            resp += str(i+1) + " "
    
    print("Teste", t)
    print(resp)
    print()

    N = input().split()
    t += 1