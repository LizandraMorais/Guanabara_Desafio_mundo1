#Desafio 13: Reajuste salarial

salario = float(input("Qual o salario do funcionario: R$"))

print("O salario que custava R${:.2f}, após o reajuste de 15% vai custar R${:.2f} ".format(salario, salario*1.15))