print("=== CADASTRO DE ALUNO ===")

nome = input("Digite o nome do aluno: ").strip()


while nome == "":
    print("o nome não pode ficar vazio.")
    nome = input("nome do aluno: ").strip()
  

while True:
    try:
        idade = int(input("Digite a idade: "))

        if idade <= 0:
            print(" A idade deve ser maior que zero.")
        else:
            break

    except ValueError:
        print("digite uma idade válida.")


notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a {i + 1}ª nota (0 a 10): "))

            if nota < 0 or nota > 10:
                print("Erro: a nota deve estar entre 0 e 10.")
            else:
                notas.append(nota)
                break

        except ValueError:
            print("Erro: digite apenas números.")


media = (notas[0] + notas[1] + notas[2]) / 3

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"


print("\n=== RESULTADO ===")

print("Nome:", nome)

print("Idade:", idade)

print("Notas:", notas)

print(f"Média: {media:.2f}")

print("Situação:", situacao)
