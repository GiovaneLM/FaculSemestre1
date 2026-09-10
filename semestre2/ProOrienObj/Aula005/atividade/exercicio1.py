import tkinter as tk
from tkinter import messagebox
from datetime import date


janela = tk.Tk()
janela.title("calculo de idade")
janela.geometry("400x300")

ano_atual = date.today().year
print(f'ano atual: {ano_atual}')

label_idade = tk.Label(janela,text='')


janela.mainloop()