alunos = []

for i in range(5):
  
    nome = input("Digite o nome do aluno ")
  
    alunos.append(nome)

duplicados = []

for nome in alunos:
  
    if alunos.count(nome) > 1 and nome not in duplicados:
      
        duplicados.append(nome)
      

if len(duplicados) > 0:
  
    print("Nomes repetidos")
  
    for nome in duplicados:
      
        print(nome)
else:
    print("Não existem nomes repetidos.")
