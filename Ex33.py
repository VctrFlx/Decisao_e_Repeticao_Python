# EXERCICIO 33
# Série 1 + 1/2 + 1/3 + ... + 1/N

n = 0
contador = 0
soma = 0.0

n = int(input("Digite N: "))

for contador in range(1, n + 1):
    soma = soma + 1 / contador

print("Resultado da série:", soma)