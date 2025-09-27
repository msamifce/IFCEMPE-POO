# Exercício 1: Classe Carro

class Carro:
    """
    Classe para representar um carro com marca, modelo, ano e cor.
    """
    def __init__(self, marca, modelo, ano, cor):
        """
        Método construtor (__init__).
        Ele inicializa os atributos do objeto quando ele é criado.
        A palavra 'self' é uma autorreferência ao próprio objeto.
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# Criando dois objetos (instâncias) da classe Carro
carro1 = Carro("Ford", "Fusion", 2020, "Preto")
carro2 = Carro("Chevrolet", "Onix", 2023, "Branco")

# Acessando e imprimindo as informações do primeiro carro
print("--- Informações do Carro 1 ---")
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Cor: {carro1.cor}")

print("\n--- Informações do Carro 2 ---")
# Acessando e imprimindo as informações do segundo carro
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")
print(f"Cor: {carro2.cor}")
