# Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
# Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = int(input("Digite uma senha."))

caracteres = senha
if caracteres >=8:
    print("Senha válida.")
else:
    print("Senha muito curta.")

# está pela metade pedir ajuda para o professor.