# Ficha 8 - Ex 2
# Dado o ano inicial e o ano final, construa o tuplo com todos os anos bissextos entre eles.


def e_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0


def anos_bissextos(inicio, fim):
    return tuple(ano for ano in range(inicio, fim + 1) if e_bissexto(ano))


ano_inicial = int(input('Ano inicial: '))
ano_final = int(input('Ano final: '))
print(anos_bissextos(ano_inicial, ano_final))
