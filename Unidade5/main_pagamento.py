# main.py
from pagamento import CartaoCredito, BoletoBancario, Pix

# Resposta à Questão:
# Como o uso de polimorfismo facilitou a implementação do sistema?
# Quais seriam as vantagens de usar uma interface abstrata nesse contexto?
"""
O polimorfismo facilitou a implementação do sistema porque o programa principal (aqui no 'main') não precisa de uma série de 'if's para verificar o tipo de pagamento. [cite_start]A lógica é centralizada na variável 'metodo_pagamento'[cite: 2195]. [cite_start]Independentemente de ser um CartaoCredito, Boleto ou Pix, o programa simplesmente chama metodo_pagamento.pagar(), e o método correto é executado automaticamente[cite: 2196].

As vantagens de usar uma classe abstrata (interface) são:
1. [cite_start]Garante consistência: Ela obriga que todas as subclasses implementem o método pagar()[cite: 1487], evitando que um método de pagamento seja criado sem a funcionalidade essencial.
2. Facilita a manutenção e expansão: Se um novo método de pagamento (ex: 'Criptomoeda') for adicionado, basta criar uma nova classe que herde de MetodoPagamento e implemente o método pagar(). Não seria necessário modificar a lógica principal do programa.
3. [cite_start]Abstração: Ela oculta os detalhes de como cada pagamento é processado, expondo apenas a API comum (o método pagar()) para o programa principal[cite: 1602].
"""

if __name__ == "__main__":
    valor_compra = float(input("Digite o valor da compra: R$ "))
    print("Selecione o método de pagamento:")
    print("1. Cartão de Crédito")
    print("2. Boleto Bancário")
    print("3. Pix")
    escolha = input("Opção: ")

    metodo_pagamento = None

    if escolha == '1':
        metodo_pagamento = CartaoCredito(valor_compra)
    elif escolha == '2':
        metodo_pagamento = BoletoBancario(valor_compra)
    elif escolha == '3':
        metodo_pagamento = Pix(valor_compra)
    else:
        print("Opção inválida.")
    
    # Se um objeto válido foi criado, chama o método pagar()
    if metodo_pagamento:
        metodo_pagamento.pagar()
