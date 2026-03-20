'''7. Ler 3 números e imprimi-los em ordem crescente.'''

print("digite o primeiro numero: ")
num1 = int(input())
print("digite o segundo numero: ")
num2 = int(input())
print("digite o terceiro numero: ")
num3 = int(input())


if(num1>num2 and num1>num3):
    if(num2>num3):
        print("a ordem crescente desses numeros é " ,num3 ," , ", num2," , ", num1)
    else:
        print("a ordem crescente desses numeros é " , num2," , ", num3," , ",num1 )

elif(num2>num1 and num2>num3):
    if(num1>num3):
        print("a ordem crescente desses numeros é " , num3," , ", num1," , ", num2)
    else:
        print("a ordem crescente desses numeros é " , num1," , ", num3," , ",num2 )

elif(num3>num1 and num3>num2):
    if(num1>num2):
        print("a ordem crescente desses numeros é " , num2," , ", num1," , ",num3 )
    else:
        print("a ordem crescente desses numeros é " , num1," , ", num2," , ",num3 )