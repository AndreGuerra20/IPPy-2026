# Ficha 3 - 3.1 Ex 3
# Verifique o resultado das conversões de número em Python.

print('(a)', int(5.6))          # 5 (trunca)
print('(b)', int(-5.6))         # -5 (trunca em direção ao zero)
print('(c)', int(9 / 5))        # 1
print('(d)', int(3e2))          # 300
print('(e)', int(3e-2))         # 0
print('(f)', float(-8))
print('(g)', float(3e2))
print('(h)', float(3e-2))
# (i) float(3+2j) -> dá erro (TypeError): não é possível converter um complexo em real.
#     Para obter a parte real usa-se (3+2j).real
print('(i)', (3 + 2j).real, '-> float(3+2j) dá TypeError')
print('(j)', float())           # 0.0
print('(k)', complex(3, 2))
print('(l)', complex(3, -2))
print('(m)', complex(3))
print('(n)', complex())         # 0j
print('(o)', complex(int(4.5), float(2)))
