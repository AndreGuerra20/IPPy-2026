# Ficha 4 - Ex 15
# Dada a média final, determine a classificação qualitativa
# (reprovado - suficiente - bom - muito bom - excelente).

nota = float(input('Média final: '))

if nota < 0 or nota > 20:
    print('Nota inválida')
elif nota < 9.5:
    print('Reprovado')
elif nota < 13.5:
    print('Suficiente')
elif nota < 15.5:
    print('Bom')
elif nota < 17.5:
    print('Muito Bom')
else:
    print('Excelente')
