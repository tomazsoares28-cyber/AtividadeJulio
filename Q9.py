nota = float(input("Digite a nota "))

if nota < 0 or nota > 10:
  
    print("Nota inválida.")
elif nota < 5:
  
    print("Desempenho ruim.")
elif nota < 7:
  
    print("Desempenho médio.")
elif nota < 9:
  
    print("Bom desempenho.")
else:
    print("Otimo desempenho.")
