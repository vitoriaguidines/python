X0, Y0, X1, Y1 = map(int, input().split())
X2, Y2, X3, Y3 = map(int, input().split())

if(X2 >= X0 and X2 <= X1):
    print(1)
elif(X3 >= X0 and X3 <= X1):
    print(1)
elif(Y2 >= Y0 and Y2 <= Y1):
    print(1)
elif(Y3 >= Y0 and Y3 <= Y1):
    print(1)
else:
    print(0)