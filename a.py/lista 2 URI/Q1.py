import sys
A = list(map(int, input().split()))
ind = sys.maxsize

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if (A[i] == A[j]):
            if(j < ind):
                ind = j
                num = A[j]

if(ind == sys.maxsize):
    print(-1)
else:
    print(num)