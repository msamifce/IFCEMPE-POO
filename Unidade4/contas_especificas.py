# contas_especificas.py
from conta import Conta

# Herança Simples: ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    """Conta Poupança: Sem funcionalidades adicionais neste exemplo."""
    def __init__(self, agencia, usuario, data_abertura, saldo):
        # Chama o construtor da classe pai (Conta)
        super().__init__(agencia, usuario, data_abertura, saldo)
        print("Conta Poupança criada.")

# Herança Simples: ContaCorrente herda de Conta
class ContaCorrente(Conta):
    """Conta Corrente: Sem funcionalidades adicionais neste exemplo."""
    def __init__(self, agencia, usuario, data_abertura, saldo):
        super().__init__(agencia, usuario, data_abertura, saldo)
        print("Conta Corrente criada.")

# Herança de Múltiplos Níveis: ContaEspecial herda de ContaCorrente
# e possui um atributo adicional (limite)
class ContaEspecial(ContaCorrente):
    """Conta Especial com limite (cheque especial)."""
    def __init__(self, agencia, usuario, data_abertura, saldo, limite):
        # Chama o construtor da classe pai (ContaCorrente)
        super().__init__(agencia, usuario, data_abertura, saldo)
        self.limite = limite
        print("Conta Especial criada.")

    # Sobrescrita de método para incluir o limite
    def sacar(self, valor):
        if valor > 0 and (valor <= self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso (incluindo limite).")
            return True
        else:
            print("Erro: Saldo + limite insuficiente ou valor inválido.")
            return False

    # Sobrescrita de método para refletir o saldo e o limite
    def consultarSaldo(self):
        saldo_total = self.saldo + self.limite
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Limite de Cheque Especial: R$ {self.limite:.2f}")
        print(f"Saldo total disponível: R$ {saldo_total:.2f}")
        return self.saldo
