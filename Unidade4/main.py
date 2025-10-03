# main.py
import random
from datetime import datetime as dt
from usuario import Usuario
from conta import Conta
from contas_especificas import ContaCorrente, ContaPoupanca, ContaEspecial

if __name__ == "__main__":
    # Instanciando um usuário
    usuario1 = Usuario(rg=12345, cpf=67890, nome="João da Silva", data_nascimento=dt(1990, 5, 15))

    # Criando e testando as contas
    print("--- Testando ContaCorrente ---")
    conta_corrente = ContaCorrente(agencia=random.randint(0, 999), usuario=usuario1, data_abertura=dt.now(), saldo=1500)
    conta_corrente.consultarSaldo()
    conta_corrente.sacar(200)
    conta_corrente.depositar(50)
    conta_corrente.consultarSaldo()

    print("\n--- Testando ContaPoupanca ---")
    conta_poupanca = ContaPoupanca(agencia=random.randint(0, 999), usuario=usuario1, data_abertura=dt.now(), saldo=3000)
    conta_poupanca.consultarSaldo()

    print("\n--- Testando ContaEspecial (Polimorfismo e Sobrescrita) ---")
    # A ContaEspecial herda e sobrescreve 'sacar' e 'consultarSaldo'
    conta_especial = ContaEspecial(agencia=random.randint(0, 999), usuario=usuario1, data_abertura=dt.now(), saldo=500, limite=2000)
    conta_especial.consultarSaldo()
    
    # Saque que usa o limite
    conta_especial.sacar(1000)
    conta_especial.consultarSaldo()
    
    # Tentando sacar um valor maior que o limite
    conta_especial.sacar(2000)
    conta_especial.consultarSaldo()
