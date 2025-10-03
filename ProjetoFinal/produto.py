# produto.py
class Produto:
    """
    Classe que representa um produto no estoque.
    Atributos:
    - __nome (privado)
    - __preco (privado)
    - __quantidade (privado)
    - total_veiculos (atributo de classe para contar os produtos)
    """
    total_produtos = 0

    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        Produto.total_produtos += 1

    # Getters usando @property para permitir apenas leitura direta
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def quantidade(self):
        return self.__quantidade

    # Setters para controlar a modificação dos atributos
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: Preço não pode ser negativo.")

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: Quantidade não pode ser negativa.")

    def adicionar_estoque(self, quantidade):
        """Incrementa a quantidade do produto."""
        self.__quantidade += quantidade
        print(f"Adicionada {quantidade} unidades de '{self.nome}'.")

    def remover_estoque(self, quantidade):
        """Decrementa a quantidade do produto, com validação simples."""
        if quantidade <= self.__quantidade:
            self.__quantidade -= quantidade
            print(f"Removida {quantidade} unidades de '{self.nome}'.")
        else:
            # Sem tratamento de exceção, apenas uma mensagem simples
            print("Erro: Quantidade para remover maior que o estoque disponível.")
    
    def __str__(self):
        """Retorna uma string formatada com as informações do produto."""
        return f"{self.nome};{self.preco};{self.quantidade}"
