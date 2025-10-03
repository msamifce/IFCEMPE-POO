# main.py
from cartao_web import DiaDosNamorados, Natal, Aniversario

# Resposta à Questão:
# Explique como ocorre o polimorfismo neste código.
"""
[cite_start]O polimorfismo ocorre porque a mesma variável 'cartao' pode referenciar objetos de diferentes classes filhas (DiaDosNamorados, Natal, Aniversario)[cite: 2221]. O método showMessage() é invocado a partir dessa única variável, mas o comportamento real do método (a mensagem exibida) é determinado em tempo de execução, de acordo com o tipo do objeto que a variável está referenciando no momento. Cada classe filha sobrescreve e implementa showMessage() de uma forma específica, mas o programa principal interage com elas de uma maneira comum, sem precisar saber o tipo exato de cada objeto.
"""

if __name__ == "__main__":
    # Cria uma instância de cada subclasse
    cartao_namorados = DiaDosNamorados("Maria")
    cartao_natal = Natal("João")
    cartao_aniversario = Aniversario("Pedro")

    # Usa uma mesma variável de referência para invocar o método
    cartao = cartao_namorados
    cartao.showMessage()

    cartao = cartao_natal
    cartao.showMessage()

    cartao = cartao_aniversario
    cartao.showMessage()
