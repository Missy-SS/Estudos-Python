class Musica:
    musicas = []
    def __init__(this, nome, artista, duracao):
        this.nome = nome
        this.artista = artista
        this.durancao = duracao
        Musica.musicas.append(this)
    
    def __str__(this):
        return f"{this.nome}, {this.artista}, {this.duracao}"
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome}, {musica.artista}")

musica1 = Musica("Under Pressure", "Queen", "248")

Musica.listar_musicas()

