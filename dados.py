import random 

input("Pressione o enter para lançar o dado")

resultado = random. randint(1,6)

print(f"O dado rolou: {resultado}")

if resultado >=6:
    print("Uau você é fera!")
elif resultado >2 <6:
    print("Está quase! Tente novamente.")
elif resultado <2:
    print("Tente novamente")
    
#finalizado