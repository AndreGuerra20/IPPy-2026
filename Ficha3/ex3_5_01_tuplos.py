# Ficha 3 - 3.5 Ex 1
# Analise o resultado dos comandos em Python.

# a)
print('(a)', (1, 'a', 2, 'b'))

# b)
tp_1 = (1, 'a', 2, 'b')
print('(b)', tp_1)

# c) os parêntesis são opcionais na criação de um tuplo
tp_2 = 1, 'a', 2, 'b'
print('(c)', tp_2)

# d) concatenação de tuplos
tp_3 = tp_2 + (3, 'c')
print('(d)', tp_3)

# e) repetição de tuplos
tp_4 = 2 * tp_2
print('(e)', tp_4)

# f) acesso por índice
tp_5 = ('Altura', 1.82, 'Peso', 78.0)
print('(f) IMC =', tp_5[3] / tp_5[1] ** 2)
