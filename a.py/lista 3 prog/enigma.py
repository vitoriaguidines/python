crip = input()
resp = input()

contador = 0

for i in range(len(crip)-len(resp)+1):
    possivel = True
    for j in range(len(resp)):
        if resp[j] == crip[i+j]:
            possivel = False
            break

    if possivel:
        contador += 1

print(contador)