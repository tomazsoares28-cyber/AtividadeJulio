try:
    arquivo = open("alunos.txt", "r")
    
    print("Arquivo encontrado!")
    conteudo = arquivo.read()
    print(conteudo)
    
    arquivo.close()

except FileNotFoundError:
    print("O arquivo 'alunos.txt' não foi encontrado.")
    print("Verifique se o arquivo existe na pasta do programa.")
