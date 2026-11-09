from veiculos import Veiculo

class Carro (Veiculo):
    def __init__(this, marca, modelo, portas):
        super().__init__(marca, modelo)
        this._portas = portas
    
    def __str__(this):
        return f"{super().__str__()} - Portas: {this._portas}"
        