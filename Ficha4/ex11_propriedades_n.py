# Ficha 4 - Ex 11
# Dado um número natural n, mostre que n² tem a mesma natureza (par/ímpar) que n,
# que n² + n é sempre par e que n³ - n é sempre divisível por 3.

n = int(input('Número natural: '))

if n <= 0:
    print('O número tem de ser natural (maior do que zero)!')
else:
    if n % 2 == 0:
        natureza_n = 'par'
    else:
        natureza_n = 'ímpar'

    if n ** 2 % 2 == 0:
        natureza_n2 = 'par'
    else:
        natureza_n2 = 'ímpar'

    print(f'{n} é {natureza_n} e {n}² = {n ** 2} é {natureza_n2}')

    if (n ** 2 + n) % 2 == 0:
        print(f'{n}² + {n} = {n ** 2 + n} é par')
    else:
        print(f'{n}² + {n} = {n ** 2 + n} não é par')

    if (n ** 3 - n) % 3 == 0:
        print(f'{n}³ - {n} = {n ** 3 - n} é divisível por 3')
    else:
        print(f'{n}³ - {n} = {n ** 3 - n} não é divisível por 3')
