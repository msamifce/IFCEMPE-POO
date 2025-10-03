# usuario.py
from datetime import datetime as dt

class Usuario:
    """
    Classe que modela um usuário com atributos RG, CPF, nome e data de nascimento.
    """
    def __init__(self, rg=0, cpf=0, nome="Padrão", data_nascimento=dt(1900, 1, 1)):
        """Método construtor com valores padrão."""
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    # Métodos modificadores (setters) para atribuir valores aos atributos
    def set_rg(self, rg):
        self.rg = rg

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_nome(self, nome):
        self.nome = nome

    def set_data_nascimento(self, dia, mes, ano):
        self.data_nascimento = dt(ano, mes, dia)

    # Métodos de acesso (getters) para obter os valores dos atributos
    def get_rg(self):
        return self.rg

    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y')
