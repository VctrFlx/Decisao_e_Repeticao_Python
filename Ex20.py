# EXERCICIO 20
# Equação de segundo grau

a = 0.0
b = 0.0
c = 0.0
delta = 0.0
raiz_delta = 0.0
x1 = 0.0
x2 = 0.0

a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

delta = b * b - 4 * a * c

raiz_delta = delta ^ 0,5

x1 = (-b + raiz_delta) / (2 * a)

x2 = (-b - raiz_delta) / (2 * a)

print("Raiz x1:", x1)
print("Raiz x2:", x2)