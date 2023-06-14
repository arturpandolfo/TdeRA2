def ler_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input("Digite um valor: "))
        vetor.append(valor)
    return vetor

def contar_pares(vetor):
    contador = 0
    for valor in vetor:
        if valor % 2 == 0:
            contador += 1
    print("Quantidade de valores que são pares:", contador)

tamanho = 10
vetor = ler_vetor(tamanho)
contar_pares(vetor)
