# EXERCICIO 25
# Duração de um jogo

hora_inicial = 0
min_inicial = 0
hora_final = 0
min_final = 0
duracao_total_min = 0
duracao_horas = 0
duracao_min = 0

hora_inicial = int(input("Digite a hora inicial: "))
min_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
min_final = int(input("Digite o minuto final: "))

hora_min_inicial = (hora_inicial * 60) + min_inicial
hora_min_final = (hora_final * 60) + min_final

if hora_min_final > hora_min_inicial:
    duracao_total_min = hora_min_final - hora_min_inicial
else:
    duracao_total_min = (hora_min_final+1440) - hora_min_inicial

if duracao_total_min >= 60:
    duracao_horas = duracao_total_min // 60
    duracao_min = duracao_total_min % 60
    print("A duração do jogo foi de", duracao_horas, "horas e", duracao_min, "minutos.")
else:
    print("A duração do jogo foi de", duracao_total_min, "minutos.")