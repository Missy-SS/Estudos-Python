from Treino.contador import contar_palavras

frase = input("Digite uma frase: ")
if not frase:
    print("Erro: Nenhuma frase foi encontrada!")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de palavras: ")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
    else:
        print("Nenhuma palavra válida foi encontrada!")