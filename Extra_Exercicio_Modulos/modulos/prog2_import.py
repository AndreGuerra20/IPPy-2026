import temperaturas as temp

n = 5
temperaturas = temp.gerar_temperaturas(5)

print(f"| {'Celsius':<10} | {'Fahrenheit':<10} | {'Classificação':<14} |")
for temperatura in temperaturas:
    print(f"| {temperatura:<10.1f} | {temp.celsius_para_fahrenheit(temperatura):<10.1f} | {temp.classificar(temperatura):<14} |")