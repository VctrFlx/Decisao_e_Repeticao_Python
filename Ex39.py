# EXERCICIO 39
# Grãos em um tabuleiro de xadrez

casa = 0
graos_casa = 1
total = 0

for casa in range(1, 65):
    print("Casa", casa, ":", graos_casa, "grão(s)")
    total = total + graos_casa
    graos_casa = graos_casa * 2

print("Total de grãos:", total)