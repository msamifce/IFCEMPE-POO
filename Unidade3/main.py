# main.py
import random
from datetime import datetime as dt
from usuario import Usuario
from conta import Conta

# a. Instanciar um objeto do tipo Usuario apenas com os valores padrão.
usuario_principal = Usuario()

# b. Solicitar a digitação dos dados do usuário
rg_input = int(input("Digite o RG do usuário: "))
cpf_input = int(input("Digite o CPF do usuário: "))
nome_input = input("Digite o nome do usuário: ")
dia_input = int(input("Digite o dia de nascimento: "))
mes_input = int(input("Digite o mês de nascimento: "))
ano_input = int(input("Digite o ano de nascimento: "))

# c. Atribuir os valores dos atributos através dos métodos modificadores.
usuario_principal.set_rg(rg_input)
usuario_principal.set_cpf(cpf_input)
usuario_principal.set_nome(nome_input)
usuario_principal.set_data_nascimento(dia_input, mes_input, ano_input)

# d. Instanciar um objeto do tipo Conta, passando valores para todos os atributos.
# A agência é gerada aleatoriamente
agencia_gerada = random.randint(0, 999)
data_abertura_hoje = dt.now()
saldo_inicial = 0.0

conta_principal = Conta(
    agencia=agencia_gerada,
    usuario=usuario_principal,
    data_abertura=data_abertura_hoje,
    saldo=saldo_inicial
)

# e. Exibir os dados da conta, incluindo os do usuário, usando métodos de acesso.
print("\n--- Informações da Conta ---")
print(f"Agência: {conta_principal.get_agencia()}")
print(f"Saldo: R$ {conta_principal.get_saldo():.2f}")
print(f"Data de Abertura: {conta_principal.get_data_abertura()}")

print("\n--- Informações do Usuário da Conta ---")
# Acessamos os dados do usuário através do objeto Conta
usuario_da_conta = conta_principal.get_usuario()
print(f"Nome: {usuario_da_conta.get_nome()}")
print(f"RG: {usuario_da_conta.get_rg()}")
print(f"CPF: {usuario_da_conta.get_cpf()}")
print(f"Data de Nascimento: {usuario_da_conta.get_data_nascimento()}")
