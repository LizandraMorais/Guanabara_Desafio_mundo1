#Desafio 20
import random  #shuffle (embaralhar) é um método para a classe

aluno1 = input("Primeiro(a) Aluno(a): ").capitalize()
aluno2 = input("Segundo(a) Aluno(a): ").capitalize()
aluno3 = input("Terceiro(a) Aluno(a): ").capitalize()
aluno4 = input("Quart(a) Aluno(a): ").capitalize()

lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)

print("A ordem de apresentação será: {}!".format(lista))