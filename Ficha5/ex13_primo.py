# Ficha 5 - Ex 13
# Dado um número natural, indique se é ou não primo.
# O ciclo pára assim que se encontra um divisor (sem usar break) e basta testar até à
# raiz quadrada do número.

numero = int(input('Número natural: '))

primo = numero > 1
divisor = 2
while primo and divisor * divisor <= numero:
    if numero % divisor == 0:
        primo = False
    divisor += 1

if primo:
    print(numero, 'é primo')
else:
    print(numero, 'não é primo')
