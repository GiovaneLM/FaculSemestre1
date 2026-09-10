import tkinter as tk #importa a biblioteca e a renomeia

##### definição do PATH caso tenha alguma diferença de  instalação
import os

# Define os caminhos onde o Tcl/Tk realmente reside no Python para Windows
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

####################################

#1.cria a janela
janela2=tk.Tk()
janela2.title('pagina auxiliar')
janela2.geometry("100x100")

janela = tk.Tk()
janela.title("Minha Primeira Janela Tkinter")
janela.geometry("400x300")

#2. adiciona um widget(por exemplo um label)
label_boas_vindas=tk.Label(janela,text='ola mundo')
label_boas_vindas.pack(pady=20)
label_local = tk.Label(janela, text="UNISENAC 2026")
label_local.pack(pady=20)
label_nome=tk.Label(janela,text='Fabio')
label_nome.pack(pady=10)



label_auxiliar=tk.Label(janela2, text='aqui janela2')
label_auxiliar.pack(pady=10)


#3.inicia o loop principal 
janela.mainloop()
janela2.mainloop()