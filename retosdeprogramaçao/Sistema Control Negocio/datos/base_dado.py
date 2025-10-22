import sqlite3
from modelo import materia_prima,produto
#from modelo.produto import Produto
class Conexcao:
    def __init__(self,bd:str):
        self.connect=sqlite3.connect(bd)
        self.cursor=self.connect.cursor()
    # Crea as tabelas que vamos definindo no sistema
    def crear_tabela(self):
        tabela="""CREATE TABLE IF NOT EXISTS PRODUTOS_COMPRADOS(
        id integer primary key autoincrement,
        nome text,
        preço real,
        cantidad integer)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        tabela="""CREATE TABLE IF NOT EXISTS ESTOQUE_PRODUTOS(
        nome text,
        cantidad integer,
        preco_medio real)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        tabela="""CREATE TABLE IF NOT EXISTS PRODUTOS(
        nome text,
        cantidad integer,
        costo real)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        tabela="""CREATE TABLE IF NOT EXISTS FUNCIONARIOS(
        nome text,
        horas_trabalhadas real,
        salario real)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        self.connect.close()
    def agregar_produto_estoque(self,nome:str,preco:float,quantidade:int):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        #na tabela estoque de productos seleccionamos a cantidade de produtos que tem que coincida com o nome passado 
        #por parametro
        self.cursor.execute("SELECT cantidad FROM ESTOQUE_PRODUTOS WHERE nome = ?",(nome,))
        cantidad=self.cursor.fetchone()
        #verificamos se ja existe
        if cantidad:
            self.cursor.execute("SELECT preco_medio FROM ESTOQUE_PRODUTOS WHERE nome = ?",(nome,))
            preco_medio=self.cursor.fetchone()
            #print(type(preco_medio))
            preco_medio=preco_medio[0]
            preco_medio=(preco_medio*cantidad[0]+quantidade*preco)/(cantidad[0]+quantidade)
            cantidad=cantidad[0]+quantidade
            self.cursor.execute("UPDATE ESTOQUE_PRODUTOS SET preco_medio = ?, cantidad = ? WHERE nome = ?",(preco_medio,cantidad,nome))
            self.connect.commit()
            self.connect.close()
        else:
            self.cursor.execute("INSERT INTO ESTOQUE_PRODUTOS(nome,preco_medio,cantidad) VALUES (?,?,?)",(nome,preco,quantidade))
            self.connect.commit()
            self.connect.close()
    #Executado quando fazemos uma compra, ele atualiza tambem o estoque 
    def AgregarProduto(self,nome:str,preco:float,quantidade:int):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        dados=(nome,preco,quantidade)
        produto="""INSERT INTO PRODUTOS_COMPRADOS(nome,preço,cantidad) VALUES (?,?,?)"""
        #estoque="""INSERT INTO ESTOQUE_PRODUTOS(nome,cantidad) VALUES (?,?)"""
        self.cursor.execute(produto,dados)
        #self.cursor.execute(estoque,(nome,quantidade))
        self.connect.commit()
        self.connect.close()
        print(f'Produto agregado corretamente')
        self.agregar_produto_estoque(nome,preco,quantidade)
    #producimos algum produto com a materia prima utilizada do estoque
    def producir(self,nome:str,cantidad:int,materia_prima:list):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        custo=0
        for materiais in materia_prima:
            custo+=Materia_Prima(materiais).get_preçomedio()*Materia_Prima(materiais).get_quantidade()
            self.cursor.execute("SELECT cantidad FROM ESTOQUE_PRODUTOS WHERE nome = ?",(Materia_Prima(materiais).get_nome),)
            cantidad_estoque=self.cursor.fetchone()[0]
            cantidad_estoque=cantidad_estoque-Materia_Prima(materiais).get_quantidade()
            self.cursor.execute("UPDATE ESTOQUE_PRODUTOS SET cantidad = ? WHERE nome = ?",(cantidad_estoque,Materia_Prima(materiais).get_nome()))
            self.connect.commit()
        self.cursor.execute("INSERT INTO PRODUTOS(nome, cantidad, costo) VALUES (?,?,?)",(nome,cantidad,custo))
        self.connect.commit()
        self.connect.close()
    #venda de proutos
    def venda_produto(self,nome:str,quantidade:int,valor_venda:float):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute("SELECT cantidad FROM PRODUTOS WHERE nome =?",(nome,))
        cantidade_previa=self.cursor.fetchone[0]
        cantidad=cantidade_previa-quantidade
        if cantidad>0:
            self.cursor.execute("UPDATE PRODUTOS SET cantidad = ? WHERE nome = ?",(cantidad,nome))
        else:
            self.cursor.execute("DELETE FROM PRODUTOS WHERE nome = ?",(nome,))
        self.connect.commit()
        self.connect.close()
    #devolve lista de materia prima
    def listar_materia_prima(self):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('SELECT * FROM ESTOQUE_PRODUTOS')
        lista_estoque=self.cursor.fetchall()
        self.connect.commit()
        self.connect.close()
        return lista_estoque
con=Conexcao('prova.db')
print(con.listar_materia_prima())