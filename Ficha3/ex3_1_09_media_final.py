# Ficha 3 - 3.1 Ex 9
# Dadas as classificações da avaliação periódica de Programação, determine a média final.
# Avaliação 2026/27: Prova Escrita 1 (30%) + Prova Escrita 2 (30%) + Trabalho Prático (40%)

prova1 = float(input('Prova Escrita 1: '))
prova2 = float(input('Prova Escrita 2: '))
trabalho = float(input('Trabalho Prático: '))

media = 0.3 * prova1 + 0.3 * prova2 + 0.4 * trabalho

print('Média final:', media)
print('Média final arredondada:', round(media))
