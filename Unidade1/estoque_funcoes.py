# estoque_funcoes.py

def adicionar_produto(estoque, nome, quantidade):
    """Adiciona ou atualiza um produto no estoque."""
    if nome in estoque:
        estoque[nome] += quantidade
        print(f"Quantidade de '{nome}' atualizada. Novo total: {estoque[nome]}")
    else:
        estoque[nome] = quantidade
        print(f"Produto '{nome}' adicionado ao estoque.")

def remover_produto(estoque, nome):
    """Remove um produto do estoque pelo nome."""
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido do estoque.")
    else:
        print("Erro: Produto não encontrado.")

def atualizar_quantidade(estoque, nome, nova_quantidade):
    """Atualiza a quantidade de um produto existente."""
    if nome in estoque:
        estoque[nome] = nova_quantidade
        print(f"Quantidade de '{nome}' atualizada para {nova_quantidade}.")
    else:
        print("Erro: Produto não encontrado para atualização.")

def exibir_estoque(estoque):
    """Exibe todos os produtos e suas quantidades."""
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\n--- ESTOQUE ATUAL ---")
        for nome, quantidade in estoque.items():
            print(f"Produto: {nome:<15} | Quantidade: {quantidade}")
        print("-" * 25)
