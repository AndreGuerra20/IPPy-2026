# Ficha 4 - Ex 23
# Dados os valores da pressão sistólica e diastólica (mm Hg), determine a classificação.
# Basta um dos valores estar num escalão para o indivíduo ficar nesse escalão ("OU"),
# por isso testa-se do escalão mais grave para o menos grave.

sistolica = int(input('Pressão sistólica (máxima): '))
diastolica = int(input('Pressão diastólica (mínima): '))

if sistolica > 180 or diastolica > 110:
    print('Crise Hipertensiva (emergência médica)')
elif sistolica >= 160 or diastolica >= 100:
    print('Pressão Arterial Elevada - Hipertensão Estágio 2')
elif sistolica >= 140 or diastolica >= 90:
    print('Pressão Arterial Elevada - Hipertensão Estágio 1')
elif sistolica >= 120 or diastolica >= 80:
    print('Pré-Hipertensão')
else:
    print('Normal')
