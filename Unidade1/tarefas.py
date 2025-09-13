# tarefas.py

from tarefas_funcoes import adicionar_tarefa, marcar_concluida, listar_tarefas

def menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar nova tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Listar todas as tarefas")
    print("4. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    lista_tarefas = [] # Lista para armazenar os dicionários de tarefas
    while True:
        opcao = menu()
        if opcao == '1':
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            adicionar_tarefa(lista_tarefas, titulo, descricao)
        elif opcao == '2':
            titulo = input("Título da tarefa a ser marcada como concluída: ")
            marcar_concluida(lista_tarefas, titulo)
        elif opcao == '3':
            listar_tarefas(lista_tarefas)
        elif opcao == '4':
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")
