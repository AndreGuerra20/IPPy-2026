# Ficha 6 - Ex 7 a) a e)
# Menu que permite calcular a área e o perímetro da circunferência (C) ou a área e o
# volume da esfera (E), com quatro casas decimais.
# (A alínea f) está nos ficheiros ex07f_modulo_circulo.py e ex07f_programa.py)
import math as mt


# a) Escrever o menu no ecrã
def print_menu():
    print("  === Menu ===")
    print(" C - Circunferência")
    print(" E - Esfera")
    print(" S - Sair")


# b) Pedir uma opção válida (aceita minúsculas)
def escolher_opcao():
    opcao = input("Escolha uma opção: ")
    while opcao.lower() not in ("c", "e", "s"):
        print("Opção inválida")
        opcao = input("Escolha uma opção: ")
    return opcao.lower()


# c) Pedir um raio válido (> 0), recebendo o texto a mostrar
def pedir_raio(textoAApresentar):
    raio = float(input(textoAApresentar))
    while raio <= 0:
        print("Raio inválido")
        raio = float(input(textoAApresentar))
    return raio


# d) Funções de cálculo
def calcular_area_circunferencia(raio):
    return mt.pi * raio ** 2


def calcular_perimetro_circunferencia(raio):
    return 2 * mt.pi * raio


def calcular_area_esfera(raio):
    return 4 * mt.pi * raio ** 2


def calcular_volume_esfera(raio):
    return (4 / 3) * mt.pi * raio ** 3


# e) Programa
def programa():
    print_menu()
    opcao = escolher_opcao()
    while opcao != "s":
        if opcao == "c":
            raio = pedir_raio("Insira o raio da circunferência: ")
            print(f"A área é: {calcular_area_circunferencia(raio):.4f}")
            print(f"O perímetro é: {calcular_perimetro_circunferencia(raio):.4f}")
        elif opcao == "e":
            raio = pedir_raio("Insira o raio da esfera: ")
            print(f"A área é: {calcular_area_esfera(raio):.4f}")
            print(f"O volume é: {calcular_volume_esfera(raio):.4f}")
        print_menu()
        opcao = escolher_opcao()


programa()
