# Ficha 6 - Ex 7 f) - MÓDULO
# Módulo com as funções das alíneas a) a d). Este ficheiro só contém funções:
# não deve ser executado diretamente, é importado por ex07f_programa.py
# (os dois ficheiros têm de estar na mesma pasta).
import math


def print_menu():
    """Escreve o menu no ecrã."""
    print("  === Menu ===")
    print(" C - Circunferência")
    print(" E - Esfera")
    print(" S - Sair")


def escolher_opcao():
    """Pede uma opção ao utilizador e devolve uma opção válida em minúsculas."""
    opcao = input("Escolha uma opção: ").lower()
    while opcao not in ("c", "e", "s"):
        print("Opção inválida")
        opcao = input("Escolha uma opção: ").lower()
    return opcao


def pedir_raio(texto):
    """Mostra o texto, pede o raio e devolve um valor válido (> 0)."""
    raio = float(input(texto))
    while raio <= 0:
        print("Raio inválido")
        raio = float(input(texto))
    return raio


def area_circunferencia(raio):
    return math.pi * raio ** 2


def perimetro_circunferencia(raio):
    return 2 * math.pi * raio


def area_esfera(raio):
    return 4 * math.pi * raio ** 2


def volume_esfera(raio):
    return 4 / 3 * math.pi * raio ** 3
