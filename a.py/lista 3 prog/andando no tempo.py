A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if(A + B == C):
    print("S")
elif(A == B):
    print("S")
elif(A + C == B):
    print("S")
elif(A == C):
    print("S")
elif(B + C == A):
    print("S")
elif(B == C):
    print("S")
else:
    print("N")