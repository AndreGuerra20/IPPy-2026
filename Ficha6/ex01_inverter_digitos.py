# Ficha 6 - Ex 1
# Função que, dado um número natural, devolve o número com os dígitos invertidos.


def inverter_digitos(numero):
    """Devolve o número com os dígitos por ordem inversa (ex: 1234 -> 4321)."""
    invertido = 0
    while numero > 0:
        invertido = invertido * 10 + numero % 10
        numero = numero // 10
    return invertido


def inverter_digitos_string(numero):
    """Alternativa usando a conversão para string."""
    return int(str(numero)[::-1])


n = int(input('Número natural: '))
print('Invertido:', inverter_digitos(n))
print('Invertido (string):', inverter_digitos_string(n))
