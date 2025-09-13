# alunos_funcoes.py

def adicionar_aluno(alunos, nome, notas):
    """Adiciona um aluno e suas notas ao dicionário."""
    alunos[nome] = notas
    print(f"Aluno '{nome}' adicionado com sucesso.")

def atualizar_notas(alunos, nome, novas_notas):
    """Atualiza as notas de um aluno existente."""
    if nome in alunos:
        alunos[nome] = novas_notas
        print(f"Notas do aluno '{nome}' atualizadas com sucesso.")
    else:
        print("Erro: Aluno não encontrado.")

def remover_aluno(alunos, nome):
    """Remove um aluno do cadastro."""
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno '{nome}' removido do cadastro.")
    else:
        print("Erro: Aluno não encontrado.")

def exibir_alunos(alunos):
    """Exibe todos os alunos e suas notas."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- CADASTRO DE ALUNOS ---")
        for nome, notas in alunos.items():
            print(f"Aluno: {nome:<15} | Notas: {notas}")
        print("-" * 25)

def calcular_media_aluno(alunos, nome):
    """Calcula e exibe a média das notas de um aluno."""
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        print(f"A média de {nome} é: {media:.2f}")
    else:
        print("Erro: Aluno não encontrado.")
