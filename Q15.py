def calcularmedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))

media = calcular_media(nota1, nota2)

print("Média:", media)


dobro = media * 2
print("Dobro da média:", dobro)
