from maquiagem import Maquiagem
from acessorios import Acessorios


batom = Maquiagem("Batom Matte", 45.00, "MQ101", 50, "Lábios", "Vermelho")
bolsa = Acessorios("Bolsa de Couro", 150.00, "AC202", 30, "Couro Ecológico", "Feminino")


batom.aplicar_desconto(10)    
 
bolsa.aplicar_desconto(15)     


batom.remover_estoque(5)
bolsa.adicionar_estoque(10)


print(" Detalhes dos Produtos:")
batom.exibir_detalhes()
bolsa.exibir_detalhes()