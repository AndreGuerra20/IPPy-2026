# Ficha 4 - Ex 7
# Dado um número inteiro superior a 100, determine o algarismo das centenas.

numero = int(input('Número inteiro superior a 100: '))

if numero > 100:
    centenas = (numero // 100) % 10
    print('Algarismo das centenas:', centenas)
else:
    print('O número tem de ser superior a 100!')
