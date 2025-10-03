# veiculo.py
class Veiculo:
    """
    Classe que representa um veículo de uma locadora.
    Contém atributos de instância, de classe, e métodos de diferentes tipos.
    """
    # Atributo de classe para contar o total de veículos
    total_veiculos = 0

    def __init__(self, placa: str, modelo: str, diaria: float):
        """
        Construtor da classe Veiculo.
        Inicializa os atributos e incrementa o contador de veículos.
        """
        # Atributos privados (duplo underline)
        self.__placa = placa
        self.__alugado = False

        # Atributos públicos
        self.modelo = modelo
        self.diaria = diaria

        # Incrementa o contador de veículos criados
        Veiculo.total_veiculos += 1

    # Propriedade de leitura para o atributo privado __placa
    @property
    def placa(self):
        """Método de acesso para a placa (getter)."""
        return self.__placa
    
    # Setter para a placa que não permite alteração
    @placa.setter
    def placa(self, nova_placa):
        """
        Método modificador para a placa (setter) que impede a alteração.
        """
        print("Aviso: A placa do veículo não pode ser alterada.")

    def alugar(self):
        """Marca o veículo como alugado, se estiver disponível."""
        if not self.__alugado:
            self.__alugado = True
            print(f"O veículo {self.modelo} ({self.placa}) foi alugado com sucesso.")
        else:
            print(f"Aviso: O veículo {self.modelo} já está alugado.")

    def devolver(self):
        """Marca o veículo como disponível, se estiver alugado."""
        if self.__alugado:
            self.__alugado = False
            print(f"O veículo {self.modelo} ({self.placa}) foi devolvido com sucesso.")
        else:
            print(f"Aviso: O veículo {self.modelo} não está alugado.")
    
    def status(self):
        """Exibe o status atual do veículo (alugado ou disponível)."""
        status_str = "alugado" if self.__alugado else "disponível"
        print(f"Status do veículo {self.modelo} ({self.placa}): {status_str}.")

    @classmethod
    def mostrar_total_veiculos(cls):
        """
        Método de classe que exibe o número total de veículos cadastrados.
        """
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias: int, diaria: float):
        """
        Método estático que calcula o preço total do aluguel.
        Não depende de nenhum atributo da instância ou da classe.
        """
        return dias * diaria

    def __str__(self):
        """Retorna uma representação em string do objeto."""
        return f"Veículo: {self.modelo} | Placa: {self.placa} | Diária: R$ {self.diaria:.2f}"
