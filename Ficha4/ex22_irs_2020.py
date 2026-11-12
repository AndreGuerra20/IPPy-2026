# Ficha 4 - Ex 22
# Dado o rendimento bruto de 2020, determine o escalão de IRS e o respetivo valor.
# Versão simplificada: aplica a taxa normal do escalão a todo o rendimento
# (não considera a parcela a abater nem as deduções).

rendimento = float(input('Rendimento bruto anual (€): '))

if rendimento < 0:
    print('Rendimento inválido')
else:
    if rendimento <= 7112:
        escalao = 1
        taxa = 14.5
    elif rendimento <= 10732:
        escalao = 2
        taxa = 23.0
    elif rendimento <= 20322:
        escalao = 3
        taxa = 28.5
    elif rendimento <= 25075:
        escalao = 4
        taxa = 35.0
    elif rendimento <= 36967:
        escalao = 5
        taxa = 37.0
    elif rendimento <= 80882:
        escalao = 6
        taxa = 45.0
    else:
        escalao = 7
        taxa = 48.0

    imposto = rendimento * taxa / 100
    print(f'Escalão: {escalao}.º  (taxa normal {taxa}%)')
    print(f'Imposto: {imposto:.2f} €')
    print(f'Rendimento após imposto: {rendimento - imposto:.2f} €')
