preco = input("Digite o preço")

if preco.strip() == "":
    print("O preço não foi informado")
else:
    try:
        preco = float(preco)
        print("Preço do produto", preco)
    except ValueError:
        print("Digite um preço válido.")
