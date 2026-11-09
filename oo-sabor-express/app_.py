from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante("praça", "gourmet")
bebida_suco = Bebida("Suco de Melancia", 5.0, "Grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Pãozinho", 2.0, "O melhor da cidade")
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == "__main__":
    main()