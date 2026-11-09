"""Exercícios
Sistema de Delivery (exercício)"""

distancia = float(input("Digite a distância até sua casa (km): ",))
taxa = 0
chuva = bool
if distancia <= 5:
    taxa = 5 
elif 5 < distancia <= 10:
    taxa = 8 
else:
    taxa = 10

if chuva == True:
    taxa = taxa + 2

print("Taxa da entrega: ", taxa)

'''Python primeira aplicação'''
print('Python na Escola de Programação Alura')
nome = input()
idade = input()
print(f'Meu nome é {nome} e tenho {idade} anos')
print("A\nL\nU\nR\nA\n")
#sep serve para especificar o separador entre os argumentos
print('A','L','U','R','A', sep='\n') 
#o separador é definido com \n, que representa uma quebra de linha

pi = 3.14159
pi_arredondado = 3.14
print(f'O valor arredondado de pi é: {pi_arredondado}')

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
