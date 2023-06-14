tamanho = 15

notas = []


for i in range(tamanho):
    nota = float(input("Digite a nota: "))
    if nota > 10:
        print("Essa nota é invalida!")
        nota = float(input("Digite a nota novamente: "))
    notas.append(nota)


soma = sum(notas)
média = soma / tamanho


print("Média Geral: ", média)
