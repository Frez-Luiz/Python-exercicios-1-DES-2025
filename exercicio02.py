#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.


Dia01 = int(input("Dias para atividade 01."))
Dia02 = int(input("Dias para atividade 02."))
Dia03 = int(input("Dias para atividade 03."))
              

if Dia01 < 0 or Dia02 < 0 or Dia03 < 0:
    print("ERRO! Número negativo.")
else:
    soma = Dia01 + Dia02 + Dia03
    print(f"Tempo total do projeto {soma} dias")