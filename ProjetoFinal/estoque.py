# estoque.py
from produto import Produto
from arquivo import salvar_produtos, carregar_produtos

class Estoque:
    def __init__(self):
        """Inicializa a lista de produtos e carrega os dados do arquivo."""
        self.produtos = carregar_produtos()

    def adicionar_produto(self, produto: Produto):
        """Adiciona um produto à lista e salva no arquivo."""
        self.produtos.append(produto)
        salvar_produtos(self.produtos)
        print(f"Produto '{produto.nome}' adicionado ao estoque.")

    def listar_produtos(self):
        """Exibe todos os produtos do estoque."""
        if not self.produtos:
            print("O estoque está vazio.")
        else:
            print("\n--- PRODUTOS EM ESTOQUE ---")
            for produto in self.produtos:
                print(f"Nome: {produto.nome:<15} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")
            print("-" * 25)

    def _obter_produto_por_nome(self, nome_produto):
        """Método auxiliar para encontrar um produto pelo nome."""
        for produto in self.produtos:
            if produto.nome == nome_produto:
                return produto
        return None

    def remover_produto(self, nome_produto: str):
        """Remove um produto do estoque e salva no arquivo."""
        produto_a_remover = self._obter_produto_por_nome(nome_produto)
        if produto_a_remover:
            self.produtos.remove(produto_a_remover)
            salvar_produtos(self.produtos)
            print(f"Produto '{nome_produto}' removido com sucesso.")
        else:
            print("Erro: Produto não encontrado.")

    def adicionar_quantidade(self, nome_produto: str, quantidade: int):
        """Adiciona uma quantidade a um produto existente e salva no arquivo."""
        produto = self._obter_produto_por_nome(nome_produto)
        if produto:
            produto.adicionar_estoque(quantidade)
            salvar_produtos(self.produtos)
        else:
            print("Erro: Produto não encontrado.")

    def remover_quantidade(self, nome_produto: str, quantidade: int):
        """Remove uma quantidade de um produto existente e salva no arquivo."""
        produto = self._obter_produto_por_nome(nome_produto)
        if produto:
            produto.remover_estoque(quantidade)
            salvar_produtos(self.produtos)
        else:
            print("Erro: Produto não encontrado.")
