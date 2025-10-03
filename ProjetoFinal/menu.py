# menu.py
def menu_principal():
    """Exibe o menu de opções do sistema."""
    print("\n--- Sistema de Gestão de Estoque ---")
    print("1. Cadastrar novo produto")
    print("2. Listar produtos")
    print("3. Adicionar quantidade a um produto")
    print("4. Remover quantidade de um produto")
    print("5. Remover produto")
    print("0. Sair")

def interagir_com_usuario(estoque):
    """Gerencia a interação do usuário e as chamadas de funções."""
    while True:
        menu_principal()
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            
            novo_produto = estoque._obter_produto_por_nome(nome)
            if novo_produto:
                print("Aviso: Produto já existe. Use a opção 'Adicionar quantidade'.")
            else:
                novo_produto = Produto(nome, preco, quantidade)
                estoque.adicionar_produto(novo_produto)
        
        elif opcao == '2':
            estoque.listar_produtos()
        
        elif opcao == '3':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            estoque.adicionar_quantidade(nome, quantidade)
        
        elif opcao == '4':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a remover: "))
            estoque.remover_quantidade(nome, quantidade)
            
        elif opcao == '5':
            nome = input("Nome do produto a remover: ")
            estoque.remover_produto(nome)

        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
