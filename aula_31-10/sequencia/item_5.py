#Item 5 -  Calcule o salário de um professor horista na Universidade XYZ.
#Entrada
hora_aula = 40
hora_mes = int(input("Quantas horas você trabalhou neste mês?"))
#Processamento
sbruto = hora_aula * hora_mes
desconto = sbruto*0.3
sliquido = sbruto - desconto
#Saída
print(f"O salário bruto do professor será R$ {sbruto}. Descontando o valor do imposto de R$ {desconto}, o salário líquido será de R$ {sliquido}.")
