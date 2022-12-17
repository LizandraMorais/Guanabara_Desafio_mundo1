# Desafio 19: Biblioteca Random-Choice
import random  # choice (escolher) é um método para a classe

aluno1 = input("Primeiro(a) Aluno(a): ").capitalize()
aluno2 = input("Segundo(a) Aluno(a): ").capitalize()
aluno3 = input("Terceiro(a) Aluno(a): ").capitalize()
aluno4 = input("Quart(a) Aluno(a): ").capitalize()

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)

print("O aluno escolhido foi: {} ".format(escolhido))

