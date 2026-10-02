alunos = ["Maria", "Joao", "Ana", "Pedro"]

posicao = int(input("Digite a posição do aluno 1 a 4: "))

if 1 <= posicao <= len(alunos):
    print("Aluno:", alunos[posicao - 1])
else:
    print("Erro, essa posição nao tem na lista .")
