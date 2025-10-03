# cartao_web.py
from abc import ABC, abstractmethod

class CartaoWeb(ABC):
    """
    Classe abstrata que representa um cartão web.
    """
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        """
        Método abstrato que deve ser implementado pelas subclasses para exibir a mensagem.
        """
        pass

class DiaDosNamorados(CartaoWeb):
    """
    Classe para cartões de Dia dos Namorados.
    """
    def showMessage(self):
        """
        Implementação do método showMessage para Dia dos Namorados.
        """
        print(f"Querido(a) {self.destinatario}, Feliz Dia dos Namorados! Com amor e carinho.")

class Natal(CartaoWeb):
    """
    Classe para cartões de Natal.
    """
    def showMessage(self):
        """
        Implementação do método showMessage para o Natal.
        """
        print(f"Caro(a) {self.destinatario}, Feliz Natal! Que o seu dia seja de paz e alegria.")

class Aniversario(CartaoWeb):
    """
    Classe para cartões de Aniversário.
    """
    def showMessage(self):
        """
        Implementação do método showMessage para Aniversário.
        """
        print(f"Parabéns, {self.destinatario}! Desejo um feliz aniversário e um ano incrível!")
