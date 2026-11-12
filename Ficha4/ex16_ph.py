# Ficha 4 - Ex 16
# Dada a concentração de iões H+ (mol/L), determine o pH = -log10(H+) e a sua
# classificação (ácido - neutro - base).
import math

concentracao = float(input('Concentração de H+ (mol/L), ex: 1e-7: '))

if concentracao <= 0:
    print('A concentração tem de ser maior do que zero!')
else:
    ph = -math.log10(concentracao)
    print(f'pH = {ph:.2f}')
    if ph < 7:
        print('Ácido')
    elif ph == 7:
        print('Neutro')
    else:
        print('Base')
