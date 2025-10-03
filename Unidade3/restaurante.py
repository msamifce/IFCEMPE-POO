# restaurante.py

class Restaurante:
    """
    Classe que modela um restaurante com nome e tipo de cozinha.
    """
    def __init__(self, nomeRestaurante, tipoCozinha):
        """Método construtor com os atributos nomeRestaurante e tipoCozinha."""
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        """Método que exibe o nome e o tipo de cozinha do restaurante."""
        print(f"Nome do Restaurante: {self.nomeRestaurante}")
        print(f"Tipo de Cozinha: {self.tipoCozinha}")
    
    def abrirRestaurante(self):
        """Método que exibe uma mensagem de restaurante aberto."""
        print(f"O restaurante {self.nomeRestaurante} está agora aberto!")

    def __str__(self):
        """
        Método mágico __str__ para retornar uma representação em string do objeto.
        """
        return f"Restaurante: {self.nomeRestaurante}, Tipo: {self.tipoCozinha}"

if __name__ == "__main__":
    # 2. Crie 3 (três) objetos Restaurante e execute o método descreverRestaurante
    print("--- Teste do método 'descreverRestaurante' ---")
    restaurante1 = Restaurante("Pizza da Vila", "Italiana")
    restaurante2 = Restaurante("Tempero Caseiro", "Brasileira")
    restaurante3 = Restaurante("Sushi Express", "Japonesa")
    
    restaurante1.descreverRestaurante()
    print("-" * 20)
    restaurante2.descreverRestaurante()
    print("-" * 20)
    restaurante3.descreverRestaurante()
    print("-" * 20)
    
    # 3. Adicione o método __str__ e utilize-o
    print("\n--- Teste do método '__str__' ---")
    print(restaurante1)
    print(restaurante2)
    print(restaurante3)
    
    restaurante1.abrirRestaurante()
