lista_convidados = set()

convidado = input("Digite o nome do convidado ou 'sair' para encerrar: " )

while convidado != "sair":
    convidado = input("Digite o nome do convidade ou 'sair' para encerrar: ")
    lista_convidados.add(convidado)


print(f"Convidades confirmados: {', '.join(lista_convidados)}") 

    