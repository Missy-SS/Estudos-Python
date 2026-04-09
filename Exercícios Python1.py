"""Número é ímpar ou par"""
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Número é par")
else:
    print("Número é ímpar")


"""Verificar se a pessoa pode ou não dirigir"""
idade = int(input("Digite sua idade: "))
tem_carteira = str(input("Digite 'sim' se possuir carteira: "))
if idade >= 18 and tem_carteira == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")


"""Verificar se a pessoa tem direito a desconto em um passe cultural"""
idade = int(input("Digite sua idade: "))
estudante = False
if idade >= 60 or estudante:
    print("Tem direito a desconto")
else:
    print("Não tem direito a desconto")


"""Verificação de Login do usuário"""
usuario_logado = False
if not usuario_logado:
    print("Faça login para continuar")


"""Verificação do direito a meia-entrada"""
idade = int(input("Digite sua idade: "))
estudante = bool(input("Digite 'sim' caso você seja um estudante: "))
if idade < 18 or estudante == True:
    print("Tem direito a meia-entrada")
else:
    print("Não tem direito a meia-entrada")
