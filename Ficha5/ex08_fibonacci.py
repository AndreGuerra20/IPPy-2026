# Ficha 5 - Ex 8
# Dado um número natural n, apresente os n primeiros termos da sucessão de Fibonacci.

n = 10

fib1 = 1
fib2 = 1
for i in range(1, n + 1):
    print(f"F{i} = {fib1}")
    aux = fib1
    fib1 = fib2
    fib2 = fib2 + aux
