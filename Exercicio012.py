#Desafio 12: Aplicação de desconto

preco = float(input("Informe o preco do produto: R$"))

print("O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f} ".format(preco, preco - ((preco*1.05) - preco)))