# pagamento.py
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    """
    Classe abstrata que representa um método de pagamento.
    """
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        """
        Método abstrato para simular o pagamento.
        """
        pass

class CartaoCredito(MetodoPagamento):
    """
    Pagamento com Cartão de Crédito (acréscimo de 5%).
    """
    def pagar(self):
        acrescimo = self.valor * 0.05
        valor_final = self.valor + acrescimo
        print("\n--- Pagamento com Cartão de Crédito ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print(f"Acréscimo de 5%: R$ {acrescimo:.2f}")
        print(f"Valor Final: R$ {valor_final:.2f}")

class BoletoBancario(MetodoPagamento):
    """
    Pagamento com Boleto Bancário (desconto de 2%).
    """
    def pagar(self):
        desconto = self.valor * 0.02
        valor_final = self.valor - desconto
        print("\n--- Pagamento com Boleto Bancário ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print(f"Desconto de 2%: R$ {desconto:.2f}")
        print(f"Valor Final: R$ {valor_final:.2f}")

class Pix(MetodoPagamento):
    """
    Pagamento com Pix (sem acréscimos ou descontos).
    """
    def pagar(self):
        print("\n--- Pagamento com Pix ---")
        print(f"Valor Original: R$ {self.valor:.2f}")
        print("Sem acréscimos ou descontos.")
        print(f"Valor Final: R$ {self.valor:.2f}")
