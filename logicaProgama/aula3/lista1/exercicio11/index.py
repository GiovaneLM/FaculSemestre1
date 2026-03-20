'''Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
                        (Fahrenheit – 32) x 5
Fórmula: Centígrados = ----------------------------
                                    9'''

print("digite a temperatura atual em Fahrenheit para ser convertido : ")
Fah = float(input())

print("Resultado : ", ((Fah - 32)*5)/9,"°C")