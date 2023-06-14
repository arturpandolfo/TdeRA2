def criar_matriz_diagonal(valor_diagonal):
    matriz = [[0] * 5 for _ in range(5)]

    for i in range(5):
        matriz[i][i] = valor_diagonal

    return matriz

matriz = criar_matriz_diagonal(7)

for linha in matriz:
    print(linha)