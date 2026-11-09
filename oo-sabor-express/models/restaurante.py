from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    
    def __init__(this, nome, categoria):
        this._nome = nome.title()
        this._categoria = categoria.title()
        this._ativo = False
        this._avaliacao = []
        this._cardapio = []
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f"{this._nome} | {this._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria do Resturante".ljust(25)} | {"Status do Restaurante"} | {"Avaliação".ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(21)} | {restaurante.media_avaliacoes}")

    @property
    def ativo(this):
        return "✔️" if this._ativo else "✗"
    
    
    def alternar_estado(this):
        this._ativo = not this._ativo
        
    def receber_avaliacao(this, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            this._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(this):
        if not this._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in this._avaliacao)
        quantidade_de_notas = len(this._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_cardapio(this, item):
        if isinstance(item, ItemCardapio):
            this._cardapio.append(item)


    @property
    def exibir_cardapio(this):
        print(f'Cardapio do restaurante {this._nome}\n')
        for i,item in enumerate(this._cardapio,start=1):
            if hasattr(item, "descricao"):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)





