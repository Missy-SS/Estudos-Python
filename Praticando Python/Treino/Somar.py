def somar (a, b):
    return a + b
try:
    num = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    resultado = somar(num, num2)

    print(resultado)
except ValueError:
    print("Erro!")