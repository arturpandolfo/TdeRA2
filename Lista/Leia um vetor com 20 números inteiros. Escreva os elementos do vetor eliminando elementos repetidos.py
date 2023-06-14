tamanho = 20
vetor = []

for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

elementos_unicos = set(vetor)

print("Elementos únicos:")
for elemento in elementos_unicos:
    print(elemento)
