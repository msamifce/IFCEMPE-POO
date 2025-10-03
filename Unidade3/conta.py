# conta.py
import random
from datetime import datetime as dt
from usuario import Usuario  # Importa a classe Usuario

class Conta:
    """
    Classe que modela uma conta bancária.
    """
    def __init__(self, agencia, usuario, data_abertura, saldo):
        """
        Método construtor que inicializa os atributos da conta.
        O atributo 'usuario' é um objeto da classe Usuario.
        """
        self.agencia = agencia
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo

    # Métodos de acesso (getters) para os atributos da conta
    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_data_abertura(self):
        return self.data_abertura.strftime('%d/%m/%Y')

    def get_saldo(self):
        return self.saldo
