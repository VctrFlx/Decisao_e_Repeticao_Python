# EXERCICIO 42
# Série 1 + 2/3 + 3/5 + ... + 50/99

numerador = 0
denominador = 0
soma = 0.0

for numerador in range(1, 51):
    denominador = 2 * numerador - 1
    soma = soma + numerador / denominador

print("Resultado da série:", soma)