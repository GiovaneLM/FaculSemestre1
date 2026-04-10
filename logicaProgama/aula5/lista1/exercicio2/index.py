'''Exercício 02.
Faça um algoritmo que imprima dez vezes o caracter "#" um ao lado do outro. Utilizando o comando for.'''
for i in range(10):
    print("#", end="")

for _ in range(10):
    print("#" , end="")
print("fim")

for _ in range(10):
    if _ == 5:
        print(_ , ";")
    print("#" , end="")
print("fim")