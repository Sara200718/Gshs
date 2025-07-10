
from produto import Produto  

class Maquiagem(Produto):
    def __init__(self, nome, preco, codigo, estoque, tipo_maquiagem, cor):
        super().__init__(nome, preco, codigo, estoque)
        self.__tipo_maquiagem = tipo_maquiagem
        self.__cor = cor

    def get_tipo_maquiagem(self):
        return self.__tipo_maquiagem

    def get_cor(self):
        return self.__cor

    # Polimorfismo
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Tipo: {self.__tipo_maquiagem}")
        print(f" Cor: {self.__cor}")
