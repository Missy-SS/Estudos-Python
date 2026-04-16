clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1  
contador = 0

while contador < 5:
    print("Bem-vindo ao Buscante!")
    contador+=1
for i in range(5):
    print("Bem-vindo ao Buscante!")
numeros = [10, 20, 30, 40, 50]
soma = 0

for numero in numeros:
    soma = soma + numero

print(f"A soma total das receitas é: {soma}")
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print("Projeto ausente")
        continue
    print(projeto)

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado:{livro}")
        break

contador = 4

while contador >= 0:
    print(f"Venda realizada! Estoque restante: {contador}")
    if contador == 0:
        print("Estoque esgotado")
    contador -= 1


