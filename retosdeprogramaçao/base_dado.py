import sqlite3
class Conexcao:
    def __init__(self,bd:str):
        self.connect=sqlite3.connect(bd)
        self.cursor=self.connect.cursor()
    def crear_tabela(self):
        tabela="""CREATE TABLE IF NOT EXISTS PRODUTOS(
        id integer primary key,
        nome text,
        preço real,
        cantidad integer)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        self.connect.close()
    def AgregarProduto(self,nome:str,preco:float,quantidade:int):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        dados=(nome,preco,quantidade)
        produto="""INSERT INTO PRODUTOS(nome,preço,cantidad) VALUES (?,?,?)"""
        self.cursor.execute(produto,dados)
        self.connect.commit()
        self.connect.close()
        print(f'Produto agregado corretamente')
prova=Conexcao('prova.db')
prova.crear_tabela()
prova.AgregarProduto('Bolacha', 5.9, 3)
