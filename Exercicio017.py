#Desafio 17: Utilizando a biblioteca emoji

import emoji
print("-" * 45)
print(emoji.emojize(":trophy: - Cálculo Hipotenusa - :trophy:",variant="emoji_type"))
print("-" * 45)

cat_opo = int(input("Digite o valor do cateto oposto: "))
cat_adj = int(input("Digite o valor do cateto adjacente: "))

hipot = sqrt( pow(cat_opo,2) + pow(cat_adj,2))

print("O valor da hipotenusa para o triângulo retângulo com cateto oposot {} e cateto adjacente {} é {}".format(cat_opo,cat_adj,math.trunc(hipot)))