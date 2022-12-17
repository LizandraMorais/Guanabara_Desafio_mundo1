# Desafio 10: Conversão real dolar

real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = 3.27
conversao = real / dolar

print("Com R${:.2f} você pode comprar US${:.2f}!".format(real, conversao))
