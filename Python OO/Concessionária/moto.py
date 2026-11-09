from veiculos import Veiculo

class Moto (Veiculo):
    def __init__(this, marca, modelo, tipo):
        super().__init__(marca, modelo)
        this._tipo = tipo
    
    def __str__(this):
        return f"{super().__str__()} - Tipo: {this._tipo}"