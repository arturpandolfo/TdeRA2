matriz =[[0] * 5 for _ in range (5)]

for i in range(5):
    matriz[i][i] = 7

for linha in matriz:
    print(linha)