x = [[0,0],[0,0]]
y = [[0,0],[0,0]]

x[0][0], y[0][0], x[0][1], y[0][1] = input().split(" ", 3)
x[1][0], y[1][0], x[1][1], y[1][1] = input().split(" ", 3)

for i in range(0, 2):
	for j in range(0, 2):
		x[i][j] = int(x[i][j])

for i in range(0, 2):
	for j in range(0, 2):
		y[i][j] = int(y[i][j])

if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1] < x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
	print(0)
else:
	print(1)