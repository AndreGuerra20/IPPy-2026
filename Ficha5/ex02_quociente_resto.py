# Ficha 5 - Ex 2
# Dado um número natural, apresente o quociente e o resto da divisão inteira desse
# número por todos os naturais inferiores a ele, excluindo o 1.

numero = int(input('Número natural: '))

for divisor in range(2, numero):
    print(f'{numero} // {divisor} = {numero // divisor}   resto = {numero % divisor}')
