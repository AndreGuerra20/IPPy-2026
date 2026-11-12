# Ficha 6 - Ex 9
# Função que recebe a massa (kg) e a altura (m) e devolve o IMC e a situação do indivíduo.
# IMC = massa / altura²


def calcular_imc(massa, altura):
    """Devolve (imc, situação) segundo a tabela da ficha."""
    imc = massa / altura ** 2
    if imc < 17:
        situacao = 'Muito abaixo do peso'
    elif imc < 18.5:
        situacao = 'Abaixo do peso'
    elif imc < 25:
        situacao = 'Peso normal'
    elif imc < 30:
        situacao = 'Acima do peso'
    elif imc < 35:
        situacao = 'Obesidade I'
    elif imc < 40:
        situacao = 'Obesidade II (severa)'
    else:
        situacao = 'Obesidade III (mórbida)'
    return imc, situacao


m = float(input('Massa (kg): '))
h = float(input('Altura (m): '))
imc, situacao = calcular_imc(m, h)
print(f'IMC = {imc:.2f} -> {situacao}')
