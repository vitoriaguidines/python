t = [[0 for x in range(3)] for y in range(3)]
p = []

t[0][0] = 0
t[0][1] = 2
t[0][2] = 4

t[1][0] = 2
t[1][1] = 0
t[1][2] = 2

t[2][0] = 4
t[2][1] = 2
t[2][2] = 0

for i in range(3):
	p.append(int(input()))

tmin = 500000
tempo = 0

for x in range(3):
	for y in range(3):
		tempo = tempo + p[y] * t[x][y]
	if(tempo < tmin):
		tmin = tempo
	tempo = 0
print(tmin)