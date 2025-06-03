# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = float(input("Digite sua distância percorrida."))
tempo = float(input("Digite seu tempo gasto."))

velocidadeM = distancia / tempo
print(f"{velocidadeM:.2f}km/h")

if velocidadeM < 5:
    print("Velocidade Lenta")
elif velocidadeM < 5 <= 10:
    print ("Velocidade Moderada")  
else:
    print("Velocidade Rápida")