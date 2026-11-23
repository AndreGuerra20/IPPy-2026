# Ficha 10 - Ex 1
# Construa o dicionário com pelo menos 4 elementos.

# a) sigla de um país europeu -> prefixo telefónico internacional
prefixos = {'PT': '+351', 'ES': '+34', 'FR': '+33', 'DE': '+49', 'IT': '+39'}

prefixos_alternativo = dict(PT='+351', ES='+34', FR='+33', DE='+49', IT='+39')
# O zip() converte os dois iteráveis em pares, que são depois convertidos em dicionário com dict()
# zip((['PT', 'ES'], ['+351', '+34'])) -> [('PT', '+351'), ('ES', '+34')]
prefixos_alternativo2 = dict(zip(['PT', 'ES', 'FR', 'DE', 'IT'], ['+351', '+34', '+33', '+49', '+39']))

# b) operação aritmética -> substantivo que a define
operacoes = {'+': 'adição', '-': 'subtração', '*': 'multiplicação', '/': 'divisão',
             '**': 'potenciação'}

# c) fruta -> quantidade em stock
stock = {'maçã': 120, 'pera': 80, 'banana': 150, 'laranja': 95}

# d) dígito -> designação em três idiomas (português, inglês, francês)
digitos = {0: ('zero', 'zero', 'zéro'),
           1: ('um', 'one', 'un'),
           2: ('dois', 'two', 'deux'),
           3: ('três', 'three', 'trois'),
           4: ('quatro', 'four', 'quatre')}

# e) número -> dia da semana (construído com o construtor dict)
dias_semana = dict([(1, 'Segunda-feira'), (2, 'Terça-feira'), (3, 'Quarta-feira'),
                    (4, 'Quinta-feira'), (5, 'Sexta-feira'), (6, 'Sábado'),
                    (7, 'Domingo')])

print('a)', prefixos)
print('a)', prefixos_alternativo)
print('a)', prefixos_alternativo2)
print('b)', operacoes)
print('c)', stock)
print('d)', digitos)
print('e)', dias_semana)
