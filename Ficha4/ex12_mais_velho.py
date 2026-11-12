# Ficha 4 - Ex 12
# Dados o nome e a idade de dois indivíduos, determine qual é o mais velho.
# Advirta o utilizador se ambos tiverem a mesma idade.

nome1 = input('Nome do 1.º indivíduo: ')
idade1 = int(input('Idade do 1.º indivíduo: '))
nome2 = input('Nome do 2.º indivíduo: ')
idade2 = int(input('Idade do 2.º indivíduo: '))

if idade1 == idade2:
    print(f'Atenção: {nome1} e {nome2} têm a mesma idade!')
elif idade1 > idade2:
    print(f'{nome1} é o mais velho')
else:
    print(f'{nome2} é o mais velho')
