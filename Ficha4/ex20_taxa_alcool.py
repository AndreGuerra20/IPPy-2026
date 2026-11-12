# Ficha 4 - Ex 20
# Dada a taxa de álcool no sangue (g/l), determine a qualificação e a respetiva coima ou
# pena (artigo 81.º do Código da Estrada).
# Nota: para condutores em regime probatório e profissionais o limite inferior é 0.2 g/l.

taxa_alcool = 0.32

if 0.5 <= taxa_alcool < 0.8:
    print("Contraordenação grave")
    print("Coima de 250€ a 1250€")
    print("Inibição de conduzir de 1 mês a 1 ano")
elif 0.8 <= taxa_alcool < 1.2:
    print("Contraordenação muito grave")
    print("Coima de 500€ a 2500€")
    print("Inibição de conduzir de 2 meses a 2 anos")
elif taxa_alcool >= 1.2:
    print("Crime")
    print("Prisão até 1 ano ou multa até 120 dias")
    print("Proibição de conduzir de 3 meses a 3 anos")
else:
    print("Sem infração (para condutores em geral)")
