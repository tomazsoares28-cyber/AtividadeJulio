entrada = input("Digite o preço")

try:
    preco = float(entrada.strip())
    quantidade = int(input("Digite a quantidade "))

    total = preco * quantidade

    print("Valor total", total)

except ValueError:
    print("Digite apenas um valor numérico válido.)
