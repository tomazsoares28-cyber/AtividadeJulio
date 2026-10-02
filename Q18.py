entrada = input("Digite o valor da compra: ")

try:
    valor = float(entrada)

    if valor < 0:
        print("o valor não pode ser negativo.")
    elif valor <= 100:
        desconto = 0
        valor_final = valor
        print("Sem desconto.")
        print("Valor final:", valor_final)
    else:
        desconto = valor * 0.10
        valor_final = valor - desconto
        print("Desconto:", desconto)
        print("Valor final:", valor_final)

except ValueError:
    print(" Digite um valor numérico válido.")
