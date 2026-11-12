# Ficha 4 - Ex 19
# Dada a temperatura corporal, determine a sua classificação.
# Tabela: <= 35 Hipotermia | 36 a 37.5 Normal | 37.8 a 39.5 Febre |
#         39.5 a 41 Febre alta | >= 41 Hipertermia
# Os intervalos ]35, 36[ e ]37.5, 37.8[ não estão na tabela: foram classificados como
# "Temperatura baixa" e "Estado subfebril".

temperatura = float(input('Temperatura (ºC): '))

if temperatura <= 35:
    print('Hipotermia')
elif temperatura < 36:
    print('Temperatura baixa')
elif temperatura <= 37.5:
    print('Normal')
elif temperatura < 37.8:
    print('Estado subfebril')
elif temperatura < 39.5:
    print('Febre')
elif temperatura < 41:
    print('Febre alta')
else:
    print('Hipertermia')
