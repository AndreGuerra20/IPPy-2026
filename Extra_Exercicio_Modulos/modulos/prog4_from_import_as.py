from temperaturas import gerar_temperaturas
from temperaturas import classificar as estado

temperaturas_7_dias = gerar_temperaturas(7)
print(temperaturas_7_dias)

n_dias_quentes = 0
for temperatura in temperaturas_7_dias:
    if estado(temperatura) == "Quente":
        n_dias_quentes += 1

print(f"Dias quentes: {n_dias_quentes}")