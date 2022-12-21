#Exercicio 21 - Utilizando o método count, split e strip em strings
nome_completo = input("Digite seu nome completo: ").strip()
print("Analisando seu nome...\n")
print("Seu nome em maiúsculas é", nome_completo.upper())
print(f"Seu nome em minúsculas é {nome_completo.lower()}")
print("Seu nome tem ao todo {}".format(len(nome_completo) - nome_completo.count(" ") ))
print(f"Seu primeiro nome é {nome_completo.split()[0]} e ele tem {len(nome_completo.split()[0])} letras")
