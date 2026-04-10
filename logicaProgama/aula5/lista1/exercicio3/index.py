'''Exercício 03.
Faça um algoritmo que leia uma frase digitada pelo usuário e imprima essa frase na tela. 
Imprima também a quantidade de caracteres digitados e q quantidades de letras ' a ' existentes.'''

frase = input("Digite uma frase: ")
print("Frase digitada: \n" , frase)
print(f"quantidade de caracteres =  {len(frase)}")
qt_a = 0
for caracter in frase:
    if caracter =='a':
        qt_a = qt_a + 1 #qt_a += 1
print(f"quantdade de a = {qt_a}")

qt_a = 0
for i in range(len(frase)):
    if frase[i] =='a':
        qt_a += 1
print(f"quantdade de a = {qt_a}")

qt_a = frase.count('a')
print(f"quantdade de a = {qt_a}")

print("Frase digitada: " , {frase})
print("Frase digitada: {}" .format(frase))



x = "Frase Digitada"
print(x)

x = "Frase Digitada"
print(x[2])

x = "Frase Digitada"
print(x[2:7])

x = "Frase Digitada"
y = x[0:5]
print(y)
print(x[2:7])


x = "Frase Digitada"
for posicao in range(len(x)):
    print(posicao , x[posicao])

x = "Frase Digitada".replace('a' , 'A')
print(x)

x=list("frase digitada")
x[0] = "P"
print(x)


while True:
    x = input("digite algo: ")
    if x.isnumeric():
        print("isto é um numero: ")
        break
    else:
        print("nao e numero:")
        

