# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

plataforma = int(input("Digite sua hora atual."))

if plataforma >9 <21:
    print("Você ainda está na carga horária")
else:
    print("Você está fora da carga horária")
