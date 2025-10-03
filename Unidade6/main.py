# main.py
from veiculo import Veiculo

if __name__ == "__main__":
    # Criar dois veículos diferentes
    carro1 = Veiculo("ABC-1234", "Ford Fusion", 150.00)
    carro2 = Veiculo("XYZ-5678", "Chevrolet Onix", 90.00)

    print("\n--- Informações Iniciais dos Veículos ---")
    print(carro1)
    print(carro2)

    # Exibir o total de veículos usando o método de classe
    print("\n--- Chamando o Método de Classe ---")
    Veiculo.mostrar_total_veiculos()

    # Alugar um veículo e exibir seu status
    print("\n--- Testando Métodos de Instância ---")
    carro1.alugar()
    carro1.status()
    
    # Devolver o veículo e exibir seu status novamente
    carro1.devolver()
    carro1.status()

    # Exibir a placa e tentar modificá-la
    print("\n--- Testando o Encapsulamento (@property) ---")
    print(f"Placa do Carro 2: {carro2.placa}")

    # A tentativa de modificação do atributo irá acionar o setter
    # que não permite a alteração e exibe a mensagem de aviso.
    carro2.placa = "DEF-9999"

    # Verificar que a placa não foi alterada
    print(f"Placa do Carro 2 após tentativa de modificação: {carro2.placa}")

    # Calcular o valor do aluguel usando o método estático
    dias_aluguel = 7
    diaria_carro2 = carro2.diaria
    preco_total = Veiculo.calcular_preco_aluguel(dias_aluguel, diaria_carro2)
    print("\n--- Chamando o Método Estático ---")
    print(f"O valor do aluguel do {carro2.modelo} por {dias_aluguel} dias é: R$ {preco_total:.2f}")
