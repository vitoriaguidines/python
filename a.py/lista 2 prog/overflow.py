N = int(input())
P, C, Q = input().split()

P = int(P)
Q = int(Q)

if(C == "*"):
    total = P * Q
elif(C == "+"):
    total = P + Q

if(total > N):
    print("OVERFLOW")
else:
    print("OK")