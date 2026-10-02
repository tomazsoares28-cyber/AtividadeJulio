cpf = input("Digite o cpf: ")

if not cpf.isdigit():
  
    print("O   CPF deve conter apenas números.")
elif len(cpf) != 11:
  
    print("O CPF deve possuir 11 dígitos.")
else:
    print("CPF válido!")
