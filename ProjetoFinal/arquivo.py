# arquivo.py

def salvar_produtos(produtos):
    """Salva os produtos em um arquivo de texto."""
    with open("produtos.txt", "w") as arquivo:
        for produto in produtos:
            arquivo.write(f"{str(produto)}\n")

def carregar_produtos():
    """Carrega os produtos do arquivo e os retorna como uma lista."""
    from produto import Produto
    produtos_carregados = []
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                if len(dados) == 3:
                    nome, preco, quantidade = dados
                    produto = Produto(nome, float(preco), int(quantidade))
                    produtos_carregados.append(produto)
        return produtos_carregados
    except FileNotFoundError:
        print("Arquivo 'produtos.txt' não encontrado. Um novo será criado.")
        return []
