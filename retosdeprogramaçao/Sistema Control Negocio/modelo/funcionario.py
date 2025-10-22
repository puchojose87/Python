class Funcionario:
    def __init__(self, nome:str):
        self.name=nome
        self.horas_trabalhadas=0.0
        self.salario=0
    def get_nome(self):
        return self.name
    def set_nome(self, novo_nome:str):
        self.name=novo_nome
    def get_horas_trabalhadas(self):
        return self.get_horas_trabalhadas
    def set_horas_trabalhadas(self, minutos:int):
        self.horas_trabalhadas+=minutos/60
    def get_salario_recebido(self):
        return self.salario
    def resever_salario(self,valor_hora:float):
        self.salario+=self.horas_trabalhadas*valor_hora
        self.set_horas_trabalhadas=0