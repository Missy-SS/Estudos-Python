class Carro:
    def __init__(this, modelo, cor, ano):
        this.modelo = modelo
        this.cor = cor
        this.ano = ano
    
    def __str__(this):
        return f"{this.modelo}, {this.cor}, {this.ano}"

    
carro1 = Carro("Mercedes", "Prata", "2025")

print(carro1)
    