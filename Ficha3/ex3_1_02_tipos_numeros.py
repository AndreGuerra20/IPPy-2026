# Ficha 3 - 3.1 Ex 2
# Verifique que os números em Python não são todos iguais.

print('(a)', type(2))
print('(b)', type(2.0))
print('(c)', type(2 + 2))
print('(d)', type(2 + 2.0))     # int + float -> float
print('(e)', type(4 // 2))      # divisão inteira entre inteiros -> int
print('(f)', type(5 // 2))
print('(g)', 5 // 2)            # 2
print('(h)', -5 // 2)           # -3 (arredonda para baixo, não para zero)
print('(i)', -3 ** 2)           # -(3 ** 2) = -9 (a potência tem prioridade sobre o sinal)
print('(j)', (-3) ** 2)         # 9
print('(k)', 2 ** 2 ** 3)       # 2 ** (2 ** 3) = 256 (a potência associa da direita para a esquerda)
print('(l)', (2 ** 2) ** 3)     # 64
