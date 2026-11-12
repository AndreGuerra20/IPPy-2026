# Ficha 3 - 3.2 Ex 1
# Determine o resultado das expressões booleanas em Python.

print('(a)', not True)
print('(b)', False and True)
print('(c)', False or True)
print('(d)', False or not True)
print('(e)', 4 > 5 or 2 < 3)
print('(f)', 3 < 17 // 2)
print('(g)', 2 < 5 < 8 < 9)
print('(h)', 1 < 3 > 6 > 2 < 10)      # 1<3 and 3>6 and ... -> False
print('(i)', True != False)
print('(j)', type(3 > 1))
print('(k)', 2 == 2.0)
print('(l)', (4 != 8) * 3)             # True vale 1 -> 3
print('(m)', (4 == 8 // 2) * 3)
print('(n)', 8 % 2 == 0)
print('(o)', -8 % 2 == 0)
print('(p)', -40 % 4 != 0)
# (q) e (r): o operador "is" compara identidade (o mesmo objeto) e não valor.
# O Python avisa (SyntaxWarning) quando se usa "is" com literais.
a, b, c = 2, 3, 2.0
print('(q)', a is not b)
print('(r)', a is c)                   # False: 2 e 2.0 são objetos diferentes
