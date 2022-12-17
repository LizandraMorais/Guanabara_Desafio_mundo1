#Desafio 4: Analisando uma string

valor = input("Escreva algo: ")
print(f"{valor}, é do tipo {type(valor)}")
print(f"É numérico? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Só tem espaços? {valor.isspace()}")
print(f"Todas as letras estão minúsculas?: {valor.islower()}")
print(f"Todas as letras estão maiúsculas?: {valor.isupper()}")
print(f"Está capitalizada?: {valor.istitle()}")