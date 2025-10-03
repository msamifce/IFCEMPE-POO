# usuario.py
from datetime import datetime as dt

class Usuario:
    def __init__(self, rg=0, cpf=0, nome="Padrão", data_nascimento=dt(1900, 1, 1)):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def set_rg(self, rg):
        self.rg = rg

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_nome(self, nome):
        self.nome = nome

    def set_data_nascimento(self, dia, mes, ano):
        self.data_nascimento = dt(ano, mes, dia)

    def get_rg(self):
        return self.rg

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y')
