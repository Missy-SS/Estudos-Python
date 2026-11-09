def calcular_idade ():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    calculo_idade = ano_atual - ano_nascimento
    print(f"A idade é {calculo_idade} anos")

calcular_idade()

#Alternativa
def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calcular_idade(nascimento, atual)
print(f"A idade é {idade} anos")
