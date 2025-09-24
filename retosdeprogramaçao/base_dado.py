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
prova=Conexcao('prova')
prova.crear_tabela()
