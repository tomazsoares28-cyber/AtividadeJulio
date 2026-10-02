temperaturas = []

quantidade = int(input("Quantas temperaturas serão digitadas? "))

for i in range(quantidade):
    temperatura = float(input("Digite a temperatura "))
    temperaturas.append(temperatura)

maior = temperaturas[0]
menor = temperaturas[0]

for temperatura in temperaturas:
    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

print("Maior temperatura", maior)
print("Menor temperatura", menor)
