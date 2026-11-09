from gorjeta_restaurante import calculo_gorjeta

valor_total = float(input("Digite o valor da conta: "))
valor_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

resultado = calculo_gorjeta(valor_total, valor_gorjeta)

print(f"{resultado:.2f}")