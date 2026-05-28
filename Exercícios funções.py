def calcular_idade ():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    calculo_idade = ano_atual - ano_nascimento
    print(f"A idade é {calculo_idade} anos")

calcular_idade()
