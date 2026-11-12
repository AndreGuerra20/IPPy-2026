# Ficha 5 - Ex 11
# Dado n, peça n números reais e apresente o maior, o menor e a média aritmética.

n = int(input('Quantos números? '))
while n <= 0:
    print('Tem de ser um número natural!')
    n = int(input('Quantos números? '))

numero = float(input('Número 1: '))
maior = numero
menor = numero
soma = numero

for i in range(2, n + 1):
    numero = float(input(f'Número {i}: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero

print('Maior:', maior)
print('Menor:', menor)
print('Média:', soma / n)
