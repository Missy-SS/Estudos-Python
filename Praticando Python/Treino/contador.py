def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip(): #se a frase não estiver vazia, 
        return {}         #separaremos as palavras
    
    palavras = frase.split()
    contagem = {}           #a chave será a palavra e o valor será a quantidade de    
                            #ocorrências na frase
    
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        #Se a palavra já existir no dicionário, somaremos 1
        #Se não, nova chave será criada com a palavra
        #e a contagem será iniciada em 1
        
    return contagem

def limpar_texto(texto):
    texto.lower()
    caracteres = ".,!?:;\"'()[]{}"
    for char in caracteres: 
        texto = texto.replace(char, "")
    return texto