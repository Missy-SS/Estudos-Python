"""Exerício 1"""
genero_favorito = str(input("Digite seu genêro músical favorito: "))
genero_musica = str(input("Digite o gênero da sua música favorita: "))

def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)

"""Exercício 2"""
idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Criança")
elif 12 <= idade <= 18:
    print("Adolescente")
else:
    print("Adulto")

"""Exercício 3"""
usuario_correto = "aluno"
senha_correto = "aluno"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correto:
    print("Login bem sucedido")
else:
    print("Usuário ou senha inválidos")

"""Exercício 4"""

valorX = float(input("Digite um valor para x: "))
valorY = float(input("Digite um valor para y: "))

if valorX > 0 and valorY > 0:
    print("Ponto se encontra no primeiro quadrante")
elif valorX < 0 and valorY > 0:
    print("Ponto se encontra no segundo quadrante")
elif valorX < 0 and valorY < 0:
    print("Ponto se encontra no terceiro quadrante")
elif valorX > 0 and valorY < 0:
    print("Ponto se encontra no quarto quadrante")
else:
    print("Ponto localizado na origem")
