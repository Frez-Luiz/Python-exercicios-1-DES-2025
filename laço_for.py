
# laço for

#Se já sabemos quantas vezes irenos repetir alguna ação. (Contar de 1 a 20)

#Situações comuns:
# Percorrer uma Lista de nomes;
# Repetár uma acão 18 vezes;
# Ler cada letra de una string(texto).

# 1º exemplo:
# imprimir os 3 primeiros dias da semana

#dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
#for dia in dias:
#   print(dia)

# laço while

# Quando não sabemos quantas vezes o códdigo deve repetir
# Situações comuns:
#   Validar senha até acertar
#   Ler dados até que um valor especifico seja digitado
#   Jogos que repetem até o jogador vencer ou perder

# 2º exemplo:
# Pedir idade até o usuário digitar um valor válido

idade = int(input("Digite sua idade (maior que 0): ") )

while idade <=0:
    print("idade invalida" )
    idade = int( input ("Tente novamente: " ))

#pronto