#Item 10 - solicite o valor de um capital, o prazo de investimento, a taxa de juros, calcule e imprima
#na tela o valor capitalizado.
#Entrada
capital = float(input("Digite o valor do capital. "))
prazo = float(input("Digite o prazo de investimento. "))
taxa_juros = float(input("Digite a taxa de juros. "))
#Processamento
capitalizado = capital + (capital*taxa_juros*prazo)
#Saída
print(capitalizado)
