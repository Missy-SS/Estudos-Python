from Banco.banco import Banco

class Agencia(Banco):
    def __init__(this, nome, endereco, numero):
        super().__init__(nome, endereco)
        this._numero = numero