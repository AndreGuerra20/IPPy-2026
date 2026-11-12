# Ficha 4 - Ex 4
# Dadas as passwords userPass e savedPass, apresente uma advertência se não forem iguais.

userPass = "password"
savedPass = "Password123456"

# Condicional simples (só a advertência)
if userPass != savedPass:
    print("Advertência: as passwords não coincidem!")

# Versão com as duas opções
if userPass == savedPass:
    print("Acesso Permitido")
else:
    print("Acesso Negado")
