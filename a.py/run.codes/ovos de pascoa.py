import math

A, B, C, D = map(int, input().split())

volume1 = A * B * C
volume2 = 4 / 3 * math.pi * (D ** 3)

diagonal = math.sqrt(float((A ** 2) + (B ** 2) + (C ** 2)))

if A >= D * 2 or B >= D * 2 or C >= D * 2 or diagonal > D * 2:
    print("N")
elif volume1 >= volume2:
    print("N")
elif volume1 <= volume2:
    print("S")