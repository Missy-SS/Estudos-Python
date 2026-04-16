A = []
NEG = []
POS = []

Numero = float(input("Digite um número (entre 0 e 50): "))
while Numero < 0 or Numero > 50:
    print("Valor inválido!")
    A.append(Numero)
    Numero = float(input("Digite um número (entre 0 e 50): "))
    if Numero >= 0 and Numero <= 50:
        A.append(Numero)
        for Numero in A:
            if Numero < 0:
                NEG.append(Numero)
            else:
                POS.append(Numero)

print(NEG)
print(len(NEG))

print(POS)
print(len(POS))


A = []
R = []

LMin = int(input("Digite um número mínimo: "))
LMax = int(input("Digite um número máximo: "))
if LMin > LMax:
    LMax = LMin
    LMin = LMax

tamanho_listaA = int(input("Digite o tamanho da lista A: "))
tamanho_listaR = int(input("Digite o tamanho da lista R: "))
while len(A) < tamanho_listaA or len(R) < tamanho_listaR:
    valores_inteiros = int(input("Digite um valor inteiro: "))
    if LMin <= valores_inteiros <= LMax:
        A.append(valores_inteiros)
    else:
        R.append(valores_inteiros)

print(A)
print(len(A))

print(R)
print(len(R))
