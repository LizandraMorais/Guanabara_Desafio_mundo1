#Desafio 11: Area de pintura x Volume de tinta

largura_parede = float(input("Largura da parede: "))
comprimento_parede = float(input("Comprimentos da parede: "))

area_parede = largura_parede * comprimento_parede

print("\nSua parede tem dimensão de {}m x {}m e área total de {} m² ".format(largura_parede, comprimento_parede,area_parede))

# 1 litro de tinta pinta 2m²

print("\nPara pintar a área de {}m² você precisará de {} litros de tinta".format(area_parede, area_parede/2))