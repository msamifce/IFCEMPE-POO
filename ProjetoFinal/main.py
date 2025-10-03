# main.py
from estoque import Estoque
from menu import interagir_com_usuario

if __name__ == "__main__":
    # Inicializa o estoque, carregando os produtos do arquivo se existirem
    estoque_loja = Estoque()
    
    # Inicia a interação com o usuário
    interagir_com_usuario(estoque_loja)
