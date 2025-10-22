from datos import base_dado
from modelo import materia_prima,produto
import tkinter as tk
from tkinter import messagebox
con=base_dado.Conexcao('prova.db')
con.crear_tabela()
def fazer_compra():
    def insertar_datos():
        #con=base_dado.Conexcao('prova.db')
        name=prod.get()
        try:
            preco=float(preco_unitario.get())
        except ValueError:
            messagebox.showwarning('Erro','O preço tem que ser um número',parent=compra_material)
            preco_unitario.delete(0,len(preco_unitario.get()))
            preco_unitario.focus_set()
            return
        cantidade=int(cantidad.get())
        con.agregar_produto_estoque(name,preco,cantidade)
        cantidad.delete(0,len(cantidad.get()))
        preco_unitario.delete(0,len(preco_unitario.get()))
        prod.delete(0,len(prod.get()))
    compra_material=tk.Tk()
    compra_material.title('Comprar Material')
    compra_material.geometry('250x200')
    nome_produto=tk.Label(compra_material,text='Material')
    #posicion do label
    nome_produto.place(x=40,y=10)
    #nome_produto.pack(pady=1)
    prod=tk.Entry(compra_material)
    prod.place(x=90,y=10)
    label_precio=tk.Label(compra_material,text='Preço Unitario')
    label_precio.place(x=10,y=50)
    preco_unitario=tk.Entry(compra_material)
    preco_unitario.place(x=90,y=50)
    label_cantidad=tk.Label(compra_material,text='Quantidade')
    label_cantidad.place(x=20,y=90)
    cantidad=tk.Entry(compra_material)
    cantidad.place(x=90,y=90)
    botao=tk.Button(compra_material,text='Comprar',command=insertar_datos)
    botao.place(x=90,y=155)

    compra_material.mainloop()
janela=tk.Tk()
janela.title('Controle Empresarial')
janela.geometry('500x400')
barra_menu=tk.Menu(janela)
janela.config(menu=barra_menu)
#item Operaçoes
menu_acao=tk.Menu(barra_menu,tearoff=0)
menu_acao.add_command(label='Fazer Compra',command=fazer_compra)
menu_acao.add_command(label='Fabricar')
menu_acao.add_command(label='Vender')
#Item funcionario
menu_funcionarios=tk.Menu(barra_menu,tearoff=0)
menu_funcionarios.add_command(label='Cadastrar Funcionario')
menu_funcionarios.add_command(label='Horas Trabalhadas')
menu_funcionarios.add_command(label='Pagar Salario')
#Controle Financiero
menu_financieiro=tk.Menu(barra_menu,tearoff=0)
menu_financieiro.add_command(label='Ingresar Saldo')
menu_financieiro.add_command(label='Fazer Emprestimo')
menu_financieiro.add_command(label='Consultar Saldo')
menu_financieiro.add_command(label='Otros Gastos')
menu_financieiro.add_command(label='Pagar Emprestimo')
barra_menu.add_cascade(label='Operações',menu=menu_acao)
barra_menu.add_cascade(label='Funcionarios',menu=menu_funcionarios)
barra_menu.add_cascade(label='Financieiro',menu=menu_financieiro)
janela.mainloop()