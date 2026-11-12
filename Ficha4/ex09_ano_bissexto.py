# Ficha 4 - Ex 9
# Dado um ano do calendário gregoriano, determine se é ou não bissexto.

ano = int(input('Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(ano, 'é bissexto')
else:
    print(ano, 'não é bissexto')
