 A, B, C = map(int, input().split())
if((A >= B + C or A <= abs(B - C)) or (B >= A + C or B <= abs(A - C)) or (C >= A + B or  C <= abs(A - B))):
    print("n")
elif(A ** 2 == B ** 2 + C ** 2 or B ** 2 == A ** 2 + C ** 2 or C ** 2 == A ** 2 + B ** 2):
    print("r")
elif(A ** 2 > B ** 2 + C ** 2 or B ** 2 > A ** 2 + C ** 2 or C ** 2 > A ** 2 + B ** 2):
    print("o")
elif(A ** 2 < B ** 2 + C ** 2 or B ** 2 < A ** 2 + C ** 2 or C ** 2 < A ** 2 + B ** 2):
    print("a")