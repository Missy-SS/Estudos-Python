def contar_vogais(frase):
    
    contagem = 0
    
    vogais = "a", "e", "i", "o", "u"
    for i in frase.lower():
        if i in vogais:
            contagem += 1
    
    return contagem

frase = input("Digite um texto: ")
print(contar_vogais(frase)) 