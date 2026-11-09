macas = int(input("Digite o número de maçãs vendidas: "))
bananas = int(input("Digite o número de bananas vendidas: "))
if macas > bananas:
    print("As maçãs tiveram mais vendas")
elif bananas > macas:
    print("As bananas tiveram mais vendas")
else:
    print("Houve empate")
  
A = int(input("Digite os dias para a atividade A: "))
B = int(input("Digite os dias para a atividade B: "))
C = int(input("Digite os dias para a atividade C: "))
if A >= 0 and B >= 0 and C >= 0:
    T = A + B + C
    print(f"Tempo total do projeto é: {T} dias")
elif A < 0 or B < 0 or C < 0:
    print("Erro: Os dias não podem ser negativos")
temperatura_atual = float(input("Digite a temperatura atual: "))
if temperatura_atual > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")
  
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Diigte sua altura (em metros): "))
IMC = peso/(altura**2)
print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= IMC < 25:
    print("Seu peso está normal")
else:
    print("Você está acima do peso")
  
despesas = float(input("Digite o total de despesas do mês (R$): "))
if despesas > 3000:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do limite do orçamento.")
  
cedo = 8
tarde = 18
hora_atual = int(input("Digite a hora atual (formato 24 horas): "))
if hora_atual < cedo or hora_atual > tarde:
    print("Acesso negado.")
else:
    print("Acesso permitido")
  
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
media = (nota_1+nota_2+nota_3)/3
print(f"Média: {media:.2f}")
if media >= 7:
    print("Aprovado!")
elif 5 <= media < 7:
    print("Recuperação.")
else:
    print("Reprovado")
  
distancia = int(input("Digite a distância percorrida (em km): "))
if distancia <= 100:
    print("Valor do pedágio é R$ 10")
elif 100 < distancia <= 200:
    print("Valor do pedágio é R$ 20")
else: 
    print("Valor do pedágio é R$ 30")
  
numero = int(input("Digite um número:"))
if numero % 2 == 0:
    print("Número é par")
else: 
    print("Número é ímpar")
  
renda_mensal = float(input("Digite o valor da sua renda mensal:"))
parcela_desejada = float(input("Digite o valor da parcela desejada:"))
R = (parcela_desejada*100)/renda_mensal
if renda_mensal > 2000 and R > 0.30:
    print("Empréstimo negado: parcela acima de 30% da renda")
elif renda_mensal > 2000 and R < 0.30:
    print("Empréstimo aprovado: parcela abaixo de 30% da renda")
else:
    print("Empréstimo negado: renda mensal abaixo do necessário")
