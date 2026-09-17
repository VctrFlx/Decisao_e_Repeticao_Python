# EXERCICIO 27
# Velocidade média em km/h

voltas = 0
extensao = 0.0
tempo = 0.0
distancia_metros = 0.0
distancia_km = 0.0
tempo_horas = 0.0
velocidade = 0.0

voltas = int(input("Número de voltas: "))
extensao = float(input("Extensão do circuito em metros: "))
tempo = float(input("Tempo em minutos: "))

distancia_metros = voltas * extensao
distancia_km = distancia_metros / 1000
tempo_horas = tempo / 60
velocidade = distancia_km / tempo_horas

print("Velocidade média:", velocidade, "km/h")