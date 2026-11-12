# Ficha 4 - Ex 10
# Dado um número inteiro, determine se é ou não nulo e, no caso de ser positivo,
# se é par ou ímpar.

numero = 3

if numero == 0:
    print("Número é nulo")
elif numero > 0:
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")
else:
    print(numero, "é negativo (não nulo)")
