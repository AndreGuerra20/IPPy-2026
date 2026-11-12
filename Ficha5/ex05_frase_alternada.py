# Ficha 5 - Ex 5
# Dados uma frase e um número natural, apresente a frase esse número de vezes,
# alternando minúsculas e maiúsculas.

frase = "Ola mundo"
num = 12
while num > 0:
    if num % 2:
        print(frase.upper())
    else:
        print(frase.lower())
    num -= 1


# Ficha 5 Ex 5 Alternativo
frase = "Ola mundo"
num = 12
for i in range(num):
    if i % 2:
        print(frase.upper())
    else:
        print(frase.lower())
