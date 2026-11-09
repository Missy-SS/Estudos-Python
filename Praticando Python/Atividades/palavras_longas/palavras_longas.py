def tamanho_palavra(frase):
    
    palavras_longas = []

    for palavra in frase.split():
        if len(palavra) > 10:
            palavras_longas.append(palavra)
            
    if palavras_longas:
        print("Palavras longas encontradas: ")
        for palavra in palavras_longas:
            print(palavra)
    
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")

frase = input("Digite sua frase: ")
print(tamanho_palavra(frase))