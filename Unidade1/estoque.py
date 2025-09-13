# estoque.py

from estoque_funcoes import adicionar_produto, remover_produto, atualizar_quantidade, exibir_estoque

def menu():
    print("\n--- GERENCIAMENTO DE ESTOQUE ---")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Atualizar quantidade")
    print("4. Exibir estoque")
    print("5. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    estoque = {} # Dicionário para armazenar o estoque
    while True:
        opcao = menu()
        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_produto(estoque, nome, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto a ser removido: ")
            remover_produto(estoque, nome)
        elif opcao == '3':
            nome = input("Nome do produto a ser atualizado: ")
            nova_quantidade = int(input("Nova quantidade: "))
            atualizar_quantidade(estoque, nome, nova_quantidade)
        elif opcao == '4':
            exibir_estoque(estoque)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")
