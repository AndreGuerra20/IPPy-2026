# Ficha 4 - Ex 13
# Dadas as classificações da avaliação periódica de Programação, determine a situação
# académica do estudante.
#
# Avaliação 2026/27: Prova Escrita 1 (30%) + Prova Escrita 2 (30%) + Trabalho Prático (40%)
# É preciso ter aprovação (>= 9.5) em todos os momentos de avaliação. Se o estudante só
# não tiver aprovação numa das provas escritas, pode repeti-la na data do exame da época
# normal.

NOTA_MINIMA = 9.5

prova1 = float(input('Prova Escrita 1: '))
prova2 = float(input('Prova Escrita 2: '))
trabalho = float(input('Trabalho Prático: '))

media = 0.3 * prova1 + 0.3 * prova2 + 0.4 * trabalho
print(f'Média: {media:.2f}')

if prova1 >= NOTA_MINIMA and prova2 >= NOTA_MINIMA and trabalho >= NOTA_MINIMA:
    print('Aprovado com', round(media), 'valores')
elif prova1 < NOTA_MINIMA and prova2 >= NOTA_MINIMA and trabalho >= NOTA_MINIMA:
    print('Pode repetir a Prova Escrita 1 na data do exame da época normal')
elif prova2 < NOTA_MINIMA and prova1 >= NOTA_MINIMA and trabalho >= NOTA_MINIMA:
    print('Pode repetir a Prova Escrita 2 na data do exame da época normal')
else:
    print('Reprovado na avaliação periódica (vai a exame)')
