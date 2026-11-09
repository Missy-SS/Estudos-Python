from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(this, nome, preco):
        this._nome = nome
        this._preco = preco
        
    @abstractclassmethod
    def aplicar_desconto(this):
        pass
        
        
#classe abstrata todas as classes derivadas precisam da aplicação do desconto

        