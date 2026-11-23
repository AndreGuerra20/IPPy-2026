# Ficha 10 - Ex 2
# Com um dos dicionários do exercício anterior (stock de fruta):

stock = {'maçã': 120, 'pera': 80, 'banana': 150, 'laranja': 95}

# a) imprimir todos os elementos
print('a)')
for fruta, quantidade in stock.items():
    print(f'   {fruta}: {quantidade}')

# b) imprimir apenas as chaves
print('b)', list(stock.keys()))

# c) inserir um novo elemento
stock['kiwi'] = 60
print('c)', stock)

# d) eliminar o segundo elemento (os dicionários mantêm a ordem de inserção)
segunda_chave = list(stock.keys())[1]
del stock[segunda_chave]          # ou stock.pop(segunda_chave)
print('d)', stock)

# e) alterar o valor de um elemento usando a chave
stock['banana'] = 200
print('e)', stock)
