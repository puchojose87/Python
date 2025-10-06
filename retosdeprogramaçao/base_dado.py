import sqlite3
class Materia_Prima:
    def __init__(self, nome, quantidade:int, preço:float):
        self.nome=nome
        self.quantidade=quantidade
        self.preço_unitario=preço
    def get_nome(self):
        return self.nome
    def get_quantidade(self):
        return self.quantidade
    def get_preçomedio(self):
        return self.preço_unitario
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
        tabela="""CREATE TABLE IF NOT EXISTS PRODUTOS(
        nome text,
        cantidad integer,
        costo real)"""
        self.cursor.execute(tabela)
        self.connect.commit()
        self.connect.close()
    def agregar_produto_estoque(self,nome:str,preco:float,quantidade:int):
        self.connect=sqlite3.connect('prova.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute("SELECT cantidad FROM ESTOQUE_PRODUTOS WHERE nome = ?",(nome,))
        cantidad=self.cursor.fetchone()
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
prova=Conexcao('prova.db')
prova.crear_tabela()
opcao=0
while opcao!='4':
    print('Seleciona uma opção: ')
    print('1. Comprar Materia Prima')
    print('2. Fabricar Produto')
    print('3. Vender Produto')
    opcao=input('4. Sair')
    match opcao:
        case '1':
            produto=input('Produto que compramos: ')
            preco=float(input('Qual o preço do produto: '))
            quantidade=int(input('Qual a quantidade do material: '))
            prova.AgregarProduto(produto,preco,quantidade)
        case '2':
            pass
        case '3':
            pass
        case _:
            break