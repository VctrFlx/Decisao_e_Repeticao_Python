# EXERCICIO 37
# Série de Fibonacci até o N-ésimo termo

n = 0
contador = 0
anterior = 0
atual = 1
proximo = 0

n = int(input("Digite a quantidade de termos: "))

for contador in range(1, n + 1):
    print(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo