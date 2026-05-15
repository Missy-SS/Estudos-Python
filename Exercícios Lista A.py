#Exercício 1
digitos = []
pesos = [6,5,4,3,2]
multiplicacao = []
soma = []


numero = int(input("Digite um núemro de 5 dígitos: "))

while  99999 > numero < 10000:
    print(f"Valor inválido!\nDigite um valor com 5 dígitos!")
    numero = int(input("Digite um número de 5 dígitos: "))

digitos.append(numero)

separacao = [int(d) for d in str(numero)]

print(separacao)

for i in range(len(separacao)):
    multiplicacao.append(pesos[i]*separacao[i])

print(multiplicacao)

soma = sum(multiplicacao)

print(soma)

somatoria = soma % 7

print(somatoria)

print(f"{numero}-{somatoria}")

#Exercício 2

#listas

digitos = []
pesos = [6,5,4,3,2]
multiplicacao = []
soma = []
códigos = []
arquivo = "Código_Verificador.txt"

numero = int(input("Digite um número: "))

while numero == 0:
    print(f"Valor inválido!")
    numero = int(input("Digite um número: "))
    
while numero != 0:
    if 10000 < numero < 30000:
            
        digitos.append(numero)

        separacao = [int(d) for d in str(numero)]

        print(separacao)

        for i in range(len(separacao)):
            multiplicacao.append(pesos[i]*separacao[i])

        print(multiplicacao)

        soma = sum(multiplicacao)

        print(soma)

        somatoria = soma % 7

        print(somatoria)

        print(f"{numero}-{somatoria}")
        
        códigos.append(f"{numero}-{somatoria}")
        

        with open(arquivo, 'a', encoding='utf-8') as file:
            for codigo in códigos:
                linha = f"{numero}-{somatoria}\n"
        
        # Grava no arquivo
            file.write(linha)
            print(f"Gravado: {linha.strip()}")
            
        print("Código gravado com sucesso!")
                
        multiplicacao.clear()
        
        numero = int(input("Digite um Código: "))
    else:
        print("Código Inválido!")

#Exercício 3

dados = []
totais = []
loop = [1]

for item in loop:
    entrada_categoria = str(input("Digite a categoria: "))
    dados.append(f"{entrada_categoria};")

    entrada_quantidade = str(input("Digite a quantidade: "))
    dados.append(f"{entrada_quantidade};")

    entrada_valor = str(input("Digite o valor: "))
    dados.append(f"{entrada_valor}")

    Qtde = float(entrada_quantidade)
    Val = float(entrada_valor)
    Total = Qtde * Val

    totais.append(Total)

    soma = sum(totais)

    for i in range(0, len(dados),3):
        print(*dados[i:i+3])

    print(f"{soma:.2f}")


    loop.append(1)
#Exercício 5
alunos = []
medias = []

N = 1

numero_inteiro = int(input("Digite a quantidade de notas: "))

while numero_inteiro <= 0:
    print("Valor precisa ser diferente e maior que zero")
    numero_inteiro = int(input("Digite a quantidade de notas: "))

while N <= numero_inteiro:
    print("Digite as notas dos alunos")
    notas_alunos = float(input(f"{N}º nota: "))
    alunos.append(notas_alunos)
    N = N + 1


soma_media = sum(alunos)
#Não precisa das médias, os números colocados já são as médias
Media = soma_media / numero_inteiro

medias.append(Media)

print(Media)

for media in medias:
    if Media > 6:
        print("Aluno ficou acima da média")
    elif Media == 6:
        print("Aluno ficou na média")
    else:
        print("Aluno ficou abaixo da média")



print(medias)


