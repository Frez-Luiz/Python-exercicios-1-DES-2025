
# Soma até digitar 0

soma = 0
numero = int(input("Digite um número (para parar a soma digite 0)") )

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (para parar a soma digite 0)"))
print ("Soma total: ", soma)

#pronto