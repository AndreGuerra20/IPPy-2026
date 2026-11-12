# Ficha 3 - 3.3 Ex 4
# Dada uma palavra, verifique se é um palíndromo.
# (Nesta fase ainda não se usa o if: o resultado é o valor lógico da comparação.)

palavra = input('Palavra: ').lower()

print('É palíndromo?', palavra == palavra[::-1])
