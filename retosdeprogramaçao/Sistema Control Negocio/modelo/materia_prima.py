class Materia_Prima:
    # Construtor da class Materia Prima, receve 3 parametros(nome,valor e quantidade)
    def __init__(self, nome:str, valor:float, quantidade:int):
        self.nome=nome
        self.valor=valor
        self.quantidade=quantidade
    # Encapsulamento dos atributos, funções get e set
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome:str):
        self.nome=novo_nome
    def get_valor(self):
        return self.valor
    def set_valor(self, novo_valor:float):
        self.valor=novo_valor
    def get_quantidade(self):
        return self.quantidade
    def set_quantidade(self,nova_quantidade:int):
        self.quantidade=nova_quantidade
