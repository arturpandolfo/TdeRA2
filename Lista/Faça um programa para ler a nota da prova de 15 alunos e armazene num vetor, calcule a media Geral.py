def calcular_media(vetor):
    soma = sum(vetor)
    media = soma / len(vetor)
    return media


def ler_notas(tamanho):
    notas = []
    for i in range(tamanho):
        nota = float(input("Digite a nota: "))
        while nota > 10:
            print("Essa nota é inválida!")
            nota = float(input("Digite a nota novamente: "))
        notas.append(nota)
    return notas


tamanho = 15
notas = ler_notas(tamanho)
media_geral = calcular_media(notas)

print("Média Geral:", media_geral)