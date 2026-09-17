# EXERCICIO 32
# Fatorial

numero = 0
contador = 0
fatorial = 1

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Não existe fatorial de número negativo.")
else:
    contador = 1

    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1

    print("Fatorial:", fatorial)