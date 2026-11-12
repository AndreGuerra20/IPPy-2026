# Ficha 3 - 3.2 Ex 2
# Usando condições booleanas, codifique em Python as afirmações.
# Os valores das variáveis são exemplos: altere-os para testar.

idade = 30
altura = 1.75
nota = 14
a, b, c = 1, -3, 2
ladoA, ladoB, ladoC = 3, 4, 5
angulo = 300
numero = 28
ano = 2024

print('(a)', type(idade) == int and 18 < idade < 65)
print('(b)', type(altura) == float and 0 < altura < 2.50)
print('(c)', 0 <= nota <= 20)
print('(d)', a != 0 and b != 0 and c != 0)
print('(e)', ladoA == ladoB == ladoC)
print('(f)', ladoA == ladoB or ladoA == ladoC or ladoB == ladoC)
print('(g)', abs(ladoA - ladoB) < ladoC < ladoA + ladoB)
print('(h)', 0 < angulo % 360 < 90)
print('(i)', 270 < angulo % 360 < 360)        # o % 360 também trata ângulos negativos
print('(j)', type(numero) == int and numero % 2 == 0 and numero % 7 == 0)
print('(k)', type(ano) == int and ano < 2050 and ano % 4 == 0)
print('(l)', (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0)
