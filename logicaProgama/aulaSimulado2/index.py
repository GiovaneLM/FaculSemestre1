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
    for i in range(qtd_professor):
        nome=input("qual o nome do nome professor: ")
        notaF=0
        for j in range(qtd_aluno):
            while True:
                try:
                    nota=int(input(f"{j+1}° Aluno Digite a nota do professoar {nome}  (entre 1 e 5): "))
                    if nota <= 5 or 1 <= nota: 
                        notaF += nota
                        break
                    else:
                        print('valor nao esta entre o intervalo digitado')
                        continue
                except:
                    print('Valor invalido')
                    continue
        media=notaF/qtd_aluno
        professores.append([nome,notaF,media])
        print(professores)
    professores.sort(key=lambda x: x[2])
    for l in range(qtd_professor):
        print(f"professor:  {professores[l][0]}  notas: {professores[l][1]}   media:  {professores[l][2]} ")
    print("Obrigado por usar nosso sistema \nAdeus")
    break


