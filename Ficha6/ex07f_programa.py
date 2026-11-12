# Ficha 6 - Ex 7 f) - PROGRAMA
# Programa que importa o módulo ex07f_modulo_circulo e executa o menu.
# Executar este ficheiro (o módulo tem de estar na mesma pasta).
import ex07f_modulo_circulo as circ

circ.print_menu()
opcao = circ.escolher_opcao()
while opcao != "s":
    if opcao == "c":
        raio = circ.pedir_raio("Insira o raio da circunferência: ")
        print(f"A área é: {circ.area_circunferencia(raio):.4f}")
        print(f"O perímetro é: {circ.perimetro_circunferencia(raio):.4f}")
    else:
        raio = circ.pedir_raio("Insira o raio da esfera: ")
        print(f"A área é: {circ.area_esfera(raio):.4f}")
        print(f"O volume é: {circ.volume_esfera(raio):.4f}")
    circ.print_menu()
    opcao = circ.escolher_opcao()
