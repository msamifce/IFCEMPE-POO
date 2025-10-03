# menu.py
from produto import Produto
from estoque import Estoque

def menu_principal():
    """Exibe o menu de opções do sistema."""
    print("\n--- Sistema de Gestão de Estoque ---")
    print("1. Cadastrar novo produto")
    print("2. Listar produtos")
    print("3. Adicionar quantidade a um produto")
    print("4. Remover quantidade de um produto")
    print("5. Remover produto")
    print("0. Sair")

def interagir_com_usuario(estoque: Estoque):
    """Gerencia a interação do usuário e as chamadas de funções."""
    while True:
        menu_principal()
        opcao = input("Digite sua opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                
                # Crie a instância de Produto dentro do menu
                novo_produto = Produto(nome, preco, quantidade)
                # Chame o método da classe Estoque para adicionar o produto à lista
                estoque.adicionar_produto(novo_produto)
            except ValueError:
                print("Entrada inválida! Preço deve ser um número e Quantidade um número inteiro.")
            
        elif opcao == '2':
            estoque.listar_produtos()
        
        elif opcao == '3':
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade a adicionar: "))
                estoque.adicionar_quantidade(nome, quantidade)
            except ValueError:
                print("Entrada inválida! A quantidade deve ser um número inteiro.")
        
        elif opcao == '4':
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade a remover: "))
                estoque.remover_quantidade(nome, quantidade)
            except ValueError:
                print("Entrada inválida! A quantidade deve ser um número inteiro.")
            
        elif opcao == '5':
            nome = input("Nome do produto a remover: ")
            estoque.remover_produto(nome)

        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
