= int(input("Digite sua idade: "))

renda = float(input("Digite sua renda: "))

cadastro = input("O cadastro está ativo? (sim/nao): ")


if idade < 18:
  
    print("Caminho 1: Usuário menor de idade.")
  
elif renda < 1500:
  
    print("Caminho 2: Renda abaixo do limite.")
  
elif cadastro.lower() == "nao":
  
    print("Caminho 3: Cadastro inativo.")
  
else:
  
    print("Caminho 4: Usuário aprovado.")
