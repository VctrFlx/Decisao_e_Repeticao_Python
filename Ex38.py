# EXERCICIO 38
# Maior e menor entre 100 números positivos

numero = 0.0
maior = 0.0
menor = 0.0
contador = 0

for contador in range(1, 101):
    numero = float(input("Digite um número positivo: "))

    while numero <= 0:
        numero = float(input("Valor inválido. Digite um número positivo: "))

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print("Maior valor:", maior)
print("Menor valor:", menor)