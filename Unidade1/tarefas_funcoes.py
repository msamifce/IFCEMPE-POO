# tarefas_funcoes.py

def adicionar_tarefa(lista_tarefas, titulo, descricao):
    """Adiciona uma nova tarefa à lista de tarefas."""
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    lista_tarefas.append(nova_tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso.")

def marcar_concluida(lista_tarefas, titulo):
    """Marca uma tarefa como concluída."""
    encontrada = False
    for tarefa in lista_tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = "Concluído"
            encontrada = True
            print(f"Tarefa '{titulo}' marcada como concluída.")
            break
    if not encontrada:
        print("Erro: Tarefa não encontrada.")

def listar_tarefas(lista_tarefas):
    """Lista todas as tarefas, separando-as por status."""
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    pendentes = [t for t in lista_tarefas if t["status"] == "Pendente"]
    concluidas = [t for t in lista_tarefas if t["status"] == "Concluído"]

    print("\n--- TAREFAS PENDENTES ---")
    if pendentes:
        for tarefa in pendentes:
            print(f"Título: {tarefa['titulo']} | Descrição: {tarefa['descricao']}")
    else:
        print("Nenhuma tarefa pendente.")

    print("\n--- TAREFAS CONCLUÍDAS ---")
    if concluidas:
        for tarefa in concluidas:
            print(f"Título: {tarefa['titulo']} | Descrição: {tarefa['descricao']}")
    else:
        print("Nenhuma tarefa concluída.")
    print("-" * 25)
