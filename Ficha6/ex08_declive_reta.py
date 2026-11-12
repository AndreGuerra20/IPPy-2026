# Ficha 6 - Ex 8
# Dadas as coordenadas de dois pontos A=(a,b) e B=(c,d), determine o declive M e a
# ordenada na origem B do segmento de reta AB.


# a) Pedir ao utilizador as coordenadas de um ponto
def ler_ponto(nome):
    print(f"Coordenadas do ponto {nome}:")
    x = float(input("  x = "))
    y = float(input("  y = "))
    return (x, y)


# b) Verificar se dois pontos são distintos
def pontos_distintos(a, b, c, d):
    """Devolve True se (a,b) e (c,d) forem pontos distintos, False caso contrário."""
    return a != c or b != d  # not(a == c and b == d)


# c) Calcular o declive M e a ordenada na origem B
def declive_ordenada(a, b, c, d):
    if a == c:  # reta vertical
        return float('inf'), None
    M = (d - b) / (c - a)
    B = b - M * a
    return M, B


# d) Programa principal
def programa():
    a, b = ler_ponto("A")
    c, d = ler_ponto("B")

    if not pontos_distintos(a, b, c, d):
        print("Erro: os pontos A e B são coincidentes, não definem uma reta.")
    else:
        M, B = declive_ordenada(a, b, c, d)

        if M == float('inf'):
            print(f"O segmento AB é vertical (x = {a}).")
            print("O declive é infinito e não existe ordenada na origem.")
        else:
            print(f"Declive M = {M}")
            print(f"Ordenada na origem B = {B}")
            print(f"Equação da reta: y = {M}x + {B}")


programa()
