# alunos.py

from alunos_funcoes import adicionar_aluno, atualizar_notas, remover_aluno, exibir_alunos, calcular_media_aluno

def menu():
    print("\n--- GERENCIAMENTO DE ALUNOS ---")
    print("1. Adicionar aluno")
    print("2. Atualizar notas de aluno")
    print("3. Remover aluno")
    print("4. Exibir todos os alunos e notas")
    print("5. Calcular média de aluno")
    print("6. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }
    
    while True:
        opcao = menu()
        if opcao == '1':
            nome = input("Nome do aluno: ")
            notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
            adicionar_aluno(alunos, nome, notas)
        elif opcao == '2':
            nome = input("Nome do aluno a ter as notas atualizadas: ")
            novas_notas = [float(input(f"Nova nota {i+1}: ")) for i in range(4)]
            atualizar_notas(alunos, nome, novas_notas)
        elif opcao == '3':
            nome = input("Nome do aluno a ser removido: ")
            remover_aluno(alunos, nome)
        elif opcao == '4':
            exibir_alunos(alunos)
        elif opcao == '5':
            nome = input("Nome do aluno para calcular a média: ")
            calcular_media_aluno(alunos, nome)
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")
