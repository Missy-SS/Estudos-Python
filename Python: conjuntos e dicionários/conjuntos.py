# conjuntos são coleções não ordenadas de elementos, sem elementos repetidos.

conjunto1 = {"eren", "evie", "angel"}

#outra forma de criar um conjunto é com a função set()

conjunto2 = set([3,4,3,1])

print(conjunto1, conjunto2)

#Conjuntos vazios

tipo = type({})
print(tipo) 

conjunto_vazio = set()
print(conjunto_vazio)

conjunto = {1, 2, 3, 4, 5}
print(conjunto)

conjunto.add(6) #adiciona elemento
print(conjunto)

conjunto.update([9, 0, 20]) #adiciona vários elementos de um vez
print(conjunto)

conjunto.remove(2) #remove elemento; se não existir, gera um KeyError
print(conjunto)

conjunto.discard(3) #remove elemento; se não existir, não gera mensagem
print(conjunto)

conjunto.pop() #remove e retorna um elemento aleatório
print(conjunto)

conjunto.clear() #remove todos os elementos
print(conjunto)

#operações entre conjuntos

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b) #união dos dois conjuntos
print (a | b) #alternativa

a.intersection(b) #interseção de dois conjuntos
print(a & b) #alternativa

a.difference(b) #diferença entre conjuntos, considerando elementos exclusivos do primeiro
print(a-b)

a.symmetric_difference(b) #diferença entre dois conjuntos, considerando elementos exclusivos de ambos conjuntos
print(a^b)

#Relações entre os conjuntos
x = {1, 2}
y = {1, 2, 3, 4}

x.issubset(y) #verifica se o conjunto é subconjunto do outro
print(x <= b) #alternativa

x.issubset(y) #verifica se o conjunto é superconjunto de outro
print(x >= y) #alternativa

x.isdisjoint(y) #verifica se os conjuntos não tem elementos em comum
print(x.isdisjoint(y))

len(x) #verifica o número de elementos de um conjunto
print(len(x))

copia = x.copy() #retorna a copia de um conjunto
print(copia)

