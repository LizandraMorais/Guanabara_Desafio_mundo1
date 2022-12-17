#Desafio 8: Convertendo medidas

medida = float(input("Digite um valor em metros: "))

med_cm = int(medida * 100)
med_mm = int(medida * 1000)

print(f"O valor {medida} metros equivale a {med_cm} centímetros e {med_mm} milímetros")