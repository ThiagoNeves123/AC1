ano = float(input("Digite um ano:"))

ano = (ano % 4 == 0)
ano = (ano % 100 == 0)
ano = (ano % 400 == 0)

print(ano)