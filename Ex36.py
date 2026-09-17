# EXERCICIO 36
# Série 1 + 1/1! + 1/2! + ... + 1/N!

n = 0
contador = 0
fatorial = 1
soma = 1.0

n = int(input("Digite N: "))

for contador in range(1, n + 1):
    fatorial = fatorial * contador
    soma = soma + 1 / fatorial

print("Resultado da série:", soma)