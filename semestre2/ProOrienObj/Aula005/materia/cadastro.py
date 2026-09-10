import tkinter as tk
from tkinter import messagebox
#################################################################################
def cadastrar_usuario():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario and senha:
        messagebox.showinfo("cadastro realizado",f"usuario:{usuario}\nsenha:{senha}")
        limpar_formulario
    else:
        messagebox.showwarning('atenção','por favor,preencha todos os campos')

def limpar_formulario():
    entry_usuario.delete(0,tk.END)
    entry_senha.delete(0,tk.END)




#################################################################################

janela = tk.Tk()
janela.title("formulario de cadastro")
janela.geometry("350x200")

#################################################################################
#label e entry para usuario
label_usuario = tk.Label(janela,text='Usuario: ')
label_usuario.grid(row=0,column=0,padx=10,pady=10,sticky="w")#sticky="w" alinha a esquerda
entry_usuario=tk.Entry(janela,width=30)
entry_usuario.grid(row=0,column=1,padx=10,pady=10)


#label e entry para senha
label_senha = tk.Label(janela,text='Senha: ')
label_senha.grid(row=1,column=0,padx=10,pady=10,sticky="w")#sticky="w" alinha a esquerda
entry_senha=tk.Entry(janela,show="*",width=30)
entry_senha.grid(row=1,column=1,padx=10,pady=10)


#botao de cadastro
botao_cadastrar = tk.Button(janela,text='cadastrar',command=cadastrar_usuario)
botao_cadastrar.grid(row=2,column=3,columnspan=2,pady=10)


botao_limpar = tk.Button(janela,text='limpar',command=limpar_formulario)
botao_limpar.grid(row=3,column=3,columnspan=2,pady=10)
#################################################################################


janela.mainloop()