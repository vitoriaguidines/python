N = int(input())

cont = 0
while N > 0:
    N -= 1
    l, c = map(int, input().split())
    if int(c) < int(l):
        cont += int(c)
print(cont)