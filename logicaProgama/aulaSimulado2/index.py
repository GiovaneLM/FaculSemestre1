"""
SIMULADO.

Competências a serem observadas:
- Conhecer os comandos/funções utilizados.
- Saber utilizar os comandos/funções corretamente
- Desenvolver uma solução viável 

Faça um algoritmo que leia o nome de até 10 professores.
Cada professor da lista receberá uma nota entre 1 e 5 de uma turma com 8 alunos.
Mostre o nome do professor a soma de suas notas e também a média de notas de cada professor em ordem crescente..

Observações:
Você deverá realizar a tarefa individualmente / grupo.
Caso tenha dificuldades, pode fazer juntamente com um colega.
    - Entregue apenas um código com o nome dos participantes.
    - Indique quem desenvolveu o código

Coloque uma observação no início do código dizendo se você utilizou ou não IA na solução.
"""

while True:
    try:
        qtd_professor=int(input("digite quantos professores teram : "))
        qtd_aluno=int(input("digite quantos alunos teram : "))
    except ValueError:
        print("valor invalido")
        continue

    professores=[]
    nota_professor=[]


    for i in range(qtd_professor):
        nome=input("qual o nome do nome professor: ")
        professores.append(nome)
        notaF=0
        for j in range(qtd_aluno):
            nota=int(input(f"{j+1}° Aluno Digite a nota do professoar {professores[i]}  (entre 1 e 5): "))
            notaF += nota
        nota_professor.append(notaF)

        print(professores)
        print(nota_professor)
    for l in range(qtd_professor) :
        print(f"professor:  {professores[l]}  notas: {nota_professor[l]}   media:  {nota_professor[l]/qtd_aluno} ")
    print("Obrigado por usar nosso sistema \nAdeus")
    break



'''
while True:
    try:
        qtd_professor=int(input("digite quantos professores teram : "))
        qtd_aluno=int(input("digite quantos alunos teram : "))
    except ValueError:
        print("valor invalido")
        continue
    nome_professor=[]
    professores=[]


    for i in range(qtd_professor):
        while True:
            nota=0
            nome=input("qual o nome do nome professor: ")
            nome_professor.append(nome)
            for j in range(qtd_aluno):
                nota=int(input(f"{j+1}° Aluno Digite a nota do professoar {nome_professor[i]}  (entre 1 e 5): "))
                nota += nota
            media=nota/qtd_aluno
            professores.append(nome,nota,media)

    professores.sort(key=lambda x: x[2])

    for l in range(qtd_professor) :
        print(f"professor:  {professores[l]}  notas: {professores[l]}   media:  {professores[l]} ")
    print("Obrigado por usar nosso sistema \nAdeus")
    break'''