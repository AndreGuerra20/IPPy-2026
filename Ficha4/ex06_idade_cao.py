# Ficha 4 - Ex 6
# Dado o número de anos de um cão, determine a idade humana
# idadeHumana = 16 * ln(idadeCão) + 31 e compare com a regra da "multiplicação por 7".
import math

idade_cao = float(input('Idade do cão (anos): '))

if idade_cao <= 0:
    print('A idade tem de ser maior do que zero!')

if idade_cao > 0:
    idade_humana = 16 * math.log(idade_cao) + 31
    idade_regra7 = idade_cao * 7
    print(f'Idade humana (fórmula): {idade_humana:.1f} anos')
    print(f'Idade humana (x 7):     {idade_regra7:.1f} anos')
    print(f'Diferença:              {abs(idade_humana - idade_regra7):.1f} anos')
