'''2. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.'''

print("digite  valor de vA  :")
vA = int(input())
print("digite valor de vB :")
vB = int(input())

print("ANTES DA TROCA vA = ", vA, " vB = " , vB)
'''TROCAR O CONTEUDO DAS VARIAVEIS'''
'''aux = vA
vA = vB
vB = aux'''
vA, vB = vB, vA #python

print("DEPOIS DA TROCA vB = ", vA, " vB = " , vB)