class Veiculo:
    def __init__(this, marca, modelo):
        this._marca = marca
        this._modelo = modelo
        this._ligado = False
    
    def __str__(this):
        status = "ligado" if this._ligado else "desligado" 
        return f"{this._marca} | {this._modelo} | Status: {status}"