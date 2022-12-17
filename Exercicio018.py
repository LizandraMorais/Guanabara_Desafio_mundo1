#Desafio 18: Biblioteca math
import math

angulo = float(input("Digite o valor do ângulo: "))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("O seno de {}° é {:.2f}".format(angulo,seno))
print("O cosseno de {}° é {:.2f}".format(angulo,cos))
print("A tangente de {}° é {:.2f}".format(angulo,tan))