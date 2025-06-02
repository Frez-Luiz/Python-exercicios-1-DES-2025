# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = int(input("Digite sua distância percorrida."))
tempo = int(input("Digite seu tempo gasto."))

velocidade = distancia / tempo
print(f"{velocidade:.2f} km/h")
if velocidade < 5:
    print("Velocidade Lenta")
elif velocidade < 10:
    print ("Velocidade Moderada")  
elif velocidade > 10:
    print("Velocidade Rápida") 
