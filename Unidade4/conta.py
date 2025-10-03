# conta.py
import random
from datetime import datetime as dt
from usuario import Usuario

class Conta:
    def __init__(self, agencia, usuario, data_abertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.data_abertura = data_abertura
        self.saldo = saldo

    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_data_abertura(self):
        return self.data_abertura.strftime('%d/%m/%Y')

    def get_saldo(self):
        return self.saldo

    def consultarSaldo(self):
        print(f"Saldo atual da conta: R$ {self.saldo:.2f}")
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Erro: Saldo insuficiente ou valor inválido.")
            return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor): # Reutiliza o método sacar
            conta_destino.depositar(valor) # Reutiliza o método depositar
            print("Transferência concluída com sucesso.")
            return True
        return False
