# Ficha 5 - Ex 21
# Dado um número inteiro positivo, calcule quantos dígitos tem. Compare a conversão para
# string com a divisão inteira por 10. A entrada de dados deve ser validada.

texto = input('Número inteiro positivo: ')
while not texto.isdigit() or int(texto) == 0:
    print('Valor inválido!')
    texto = input('Número inteiro positivo: ')

numero = int(texto)

# 1) Conversão para string
digitos_string = len(str(numero))

# 2) Divisão inteira por 10
digitos_divisao = 0
n = numero
while n > 0:
    n = n // 10
    digitos_divisao += 1

print('Dígitos (string):  ', digitos_string)
print('Dígitos (divisão): ', digitos_divisao)
