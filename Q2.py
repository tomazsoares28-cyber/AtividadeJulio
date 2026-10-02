soma = float(input("Digite a soma das notas: "))
quantidadenotas = int(input("Digite a quantidade de notas: "))

if quantidadenotas == 0:
    print("Não é possível dividir por zero.")
else:
    medianotas = soma / quantidadenotas
    print("Média:", medianotas)
