# Exercício 2: Classe Livro

class Livro:
    """
    Classe para representar um livro com título, autor, ano de publicação e preço.
    """
    def __init__(self, titulo, autor, ano_publicacao, preco):
        """
        Método construtor que inicializa os atributos do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

# Criando dois objetos (instâncias) da classe Livro
livro1 = Livro("Use a Cabeça! Python", "Paul Barry", 2018, 95.50)
livro2 = Livro("Curso Intensivo de Python", "Eric Matthes", 2019, 120.00)

# Imprimindo as informações do primeiro livro no formato solicitado
print("\n--- Informações do Livro 1 ---")
print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco:.2f}")

# Imprimindo as informações do segundo livro no formato solicitado
print("\n--- Informações do Livro 2 ---")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco:.2f}")
