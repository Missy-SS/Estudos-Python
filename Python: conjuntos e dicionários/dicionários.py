#Estruturas de dados que armazenam pares de chave-valor

dic1 = {"nome": "Eren", "idade": "19"}

#função dict()

dic2 = dict(nome="Evie", idade=19)

print(dic1)
print(dic2)

#Dicionários vazios
dicionario = {}
dicionario = dict()

#Criando dicionários com listas de tuplas

lista_de_tuplas = [("nome", "Shade"), ("idade", 19)]
dicionario = dict(lista_de_tuplas)
print(dicionario)

#Tipos permitidos para chaves e valores

#Chaves dos dicionários devem ser valores imutáveis

dicionario_valido ={1: "um", "dois": 2, (3, 4): "par"}
print(dicionario_valido)

# dicionario_invalido = {[1, 2]: "lista"}

#Os valores podem ser de qualquer tipo de dado

dicionario = {
    "nome": "Peter",
    "idade": "22",
    "apelido": "Homem-aranha",
    "endereço": {"cidade": "Nova York", "bairro": "Queens"}
}

print(dicionario)

#acessando e modificando elementos
dic = {"nome": "Ana", "nota": 10.0}

dic["nome"] #acessar um valor por uma chave
print(dic)

dic["nota"] = 9.2 #atribui um valor a uma chave
print(dic)

del dic["nome"] #remover um item específico
print(dic)
dic["nota"] = 10.0

#métodos de manipulação de acesso e verificação

dicionario.keys() #retorna as chaves do dicionário

print(dicionario.keys())

dicionario.values() # retorna os valores do dicionário
print(dicionario.values())

dicionario.items() #retorna pares(chave, valor) como tuplas
print(dicionario.items())

len(dicionario) #conta quantos pares o dicionário possui
print(len(dicionario))

#métodos de manipulação de busca e modificação de elementos

dicionario.get("nome") # obtém um valor sem erro se a chave não existir
print(dicionario.get("nome"))

dicionario.pop("nome") #remove uma chave e retorna seu valor
print(dicionario)

chaves = list(dicionario) #usada para obter todas as chaves do dicionário em forma de lista
print(chaves)

dicionario.clear() #apaga todos os itens do dicionario

#métodos de manipulação para atualizar e remover

dicionario = {"a": 1, "b": 2, "c": 3}

dicionario.popitem() #remove e retorna o último par(chave, valor)

print(list(reversed(dicionario))) #retorna um iterador sobre as chaves do dicionário em ordem reversa 

dicionario.update({"a": 1.0, "d": 4}) #Atualiza o dicionário com outro mapeamento

copia = dicionario.copy() #retorna uma cópia rasa do dicionário
print(copia)

#Integrando conjuntos e dicionários

estoque = {
    "frutas" : {"maçã", "uva"},
    "verduras" : {"cenoura", "alface"}
}

print(estoque)

estoque["frutas"].add("morango")
estoque["verduras"].discard("alface")

print(estoque)
