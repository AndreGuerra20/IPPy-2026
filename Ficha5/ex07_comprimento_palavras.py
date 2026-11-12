# Ficha 5 - Ex 7
# Dados uma frase e um número natural, apresente o número de palavras da frase com
# comprimento igual, menor ou maior a esse número.

frase = input('Frase: ')
n = int(input('Número natural: '))

iguais = 0
menores = 0
maiores = 0

for palavra in frase.split():
    if len(palavra) == n:
        iguais += 1
    elif len(palavra) < n:
        menores += 1
    else:
        maiores += 1

print('Palavras com comprimento igual a', n, ':', iguais)
print('Palavras com comprimento menor que', n, ':', menores)
print('Palavras com comprimento maior que', n, ':', maiores)
