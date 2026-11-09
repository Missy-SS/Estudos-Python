#for: usado quando se sabe o número de iterações que devem ser realizadas. Bom para percorrer elementos.
#while: usado quando o número de iterações é deconhecido. Continua executando enquanto for verdadeiro.

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)
