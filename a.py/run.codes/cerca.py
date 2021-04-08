N, H = map(int, input().split())
A = list(map(int, input().split()))

dif = 0
mov = 0

for i in range(len(A)-1):
    if A[i] < H:
        dif = H - A[i]
        A[i] += dif
        A[i+1] += dif
        mov += dif
    elif A[i] > H:
        dif = A[i] - H
        A[i] -= dif
        A[i+1] -= dif
        mov += dif    

print(mov)