# EXERCICIO 45
# Série 1 - 2/4 + 3/9 - 4/16 + ... + 15/225

numerador = 0
denominador = 0
soma = 0.0
termo = 0.0

for numerador in range(1, 16):
    denominador = numerador * numerador
    termo = numerador / denominador

    if numerador % 2 == 0:
        soma = soma - termo
    else:
        soma = soma + termo

print("Resultado da série:", soma)