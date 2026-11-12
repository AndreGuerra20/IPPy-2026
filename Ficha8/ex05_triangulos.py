# Ficha 8 - Ex 5
# Construa o tuplo com os três lados de um triângulo até que o utilizador indique o
# tuplo nulo (0, 0, 0). Para cada triângulo apresente a classificação quanto aos lados,
# o perímetro e a área (fórmula de Héron).
import math


def pedir_lados():
    """Pede os três lados e devolve-os num tuplo."""
    print('Lados do triângulo (0 0 0 para terminar)')
    a = float(input('  a = '))
    b = float(input('  b = '))
    c = float(input('  c = '))
    return (a, b, c)


def e_triangulo(lados):
    a, b, c = lados
    return abs(a - b) < c < a + b


def classificar(lados):
    a, b, c = lados
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    return 'Escaleno'


def area_heron(lados):
    a, b, c = lados
    p = sum(lados) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def construir_triangulos():
    triangulos = ()
    lados = pedir_lados()
    while lados != (0, 0, 0):
        if e_triangulo(lados):
            triangulos += (lados,)
        else:
            print('Estes comprimentos não formam um triângulo!')
        lados = pedir_lados()
    return triangulos


triangulos = construir_triangulos()
for t in triangulos:
    print(f'{t}: {classificar(t)}, perímetro = {sum(t):.2f}, área = {area_heron(t):.2f}')
