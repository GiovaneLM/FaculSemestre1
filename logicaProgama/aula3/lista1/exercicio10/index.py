'''10. Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
                                (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
                                                        soma dos pesos'''


print("digite o valor da sua 1° nota da  materia : ")
nota1 = float(input())
print("digite o valor do peso dessa  nota : ")
peso1 = float(input())
print("digite o valor da sua 2° nota da  materia : ")
nota2 = float(input())
print("digite o valor do peso dessa  nota : ")
peso2 = float(input())


print("o calculo da sua media das notas é : ((nota 1 x peso da nota)+(nota 2 * peso da nota 2 )) / soma dos pesos")
print("nesse caso o calculo sera : ((", nota1 ," x " , peso1,") + (", nota2 , " x ", peso2,") ) / (",peso1,"+",peso2,")" )
print("resultado : ", ((nota1*peso1)+(nota2*peso2))/(peso1+peso2))