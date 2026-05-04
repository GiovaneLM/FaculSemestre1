#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

coluna = 5
string = ""
for linha in range(1, coluna + 1):
    string = str(linha) + " " + string
    print(string)