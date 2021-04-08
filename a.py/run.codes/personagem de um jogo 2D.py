N = int(input())
inicial = 0
instrucoes = []
for i in range(N):
    X = int(input())
    for j in range(X):
        inst = input()
        instrucoes.append(inst)
    for k in instrucoes:
        if(k == "ESQ"):
            inicial -= 1
        elif(k == "DIR"):
            inicial += 1
        else:
            exec_num = k.split()
            exec_num = int(exec_num[1])
            while(instrucoes[exec_num - 1] != "ESQ" and instrucoes[exec_num - 1] != "DIR"):
                exec_num = instrucoes[exec_num - 1].split()
                exec_num = int(exec_num[1])
            if(instrucoes[exec_num - 1] == "ESQ"):
                inicial -= 1
            elif(instrucoes[exec_num - 1] == "DIR"):
                inicial += 1
    print(inicial)
    instrucoes = []
    inicial = 0