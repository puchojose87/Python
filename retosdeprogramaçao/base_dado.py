import sqlite3
class Conexcao:
    def __init__(self,bd:str):
        self.connect=sqlite3.connect(bd)
        self.cursor=self.connect.cursor()
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
        self.connect.close()
    def AgregarProduto(self,nome:str,preco:float,quantidade:int):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        dados=(nome,preco,quantidade)
        produto="""INSERT INTO PRODUTOS_COMPRADOS(nome,preço,cantidad) VALUES (?,?,?)"""
        estoque="""INSERT INTO ESTOQUE_PRODUTOS(nome,cantidad) VALUES (?,?)"""
        self.cursor.execute(produto,dados)
        self.cursor.execute(estoque,(nome,quantidade))
        self.connect.commit()
        self.connect.close()
        print(f'Produto agregado corretamente')
prova=Conexcao('prova.db')
prova.crear_tabela()
produto=input('Produto que compramos: ')
preco=float(input('Qual o preço do produto: '))
quantidade=int(input('Qual a quantidade do material: '))
prova.AgregarProduto(produto,preco,quantidade)
