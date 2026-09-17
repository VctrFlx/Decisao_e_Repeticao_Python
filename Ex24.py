# EXERCICIO 24
# Números divisíveis por 2 e 3

numero = 0

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(numero,"é divisível por 2 e por 3.")
elif numero % 2 == 0:
    print(numero,"é divisível somente por 2.")
elif numero % 3 == 0:
    print(numero,"é divisível somente por 3.")
else:
    print(numero,"não é divisível por 2 nem 3.")