from modelo.materia_prima import Materia_Prima
class Produto:
    def __init__(self,nome:str,preço:float,quantidade:int,lista_materiais):
        self.materiais_utilizados[Materia_Prima]=lista_materiais
        self.nome=nome
        self.preço=preço
        self.quantidade=quantidade
        self.costo=0.0
        if len(lista_materiais)>0:
            for material in lista_materiais:
                self.costo=self.costo+(Materia_Prima(material).get_quantidade()*Materia_Prima(material).get_valor())
    
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome:str):
        self.nome=novo_nome
    def get_quantidade(self):
        return self.quantidade
    def set_quantidade(self,nova_quantidade:int):
        self.quantidade=nova_quantidade
    def get_costo(self):
        return self.costo
    def get_preço(self):
        return self.preço
    def set_valor(self, novo_preço:float):
        self.valor=novo_preço