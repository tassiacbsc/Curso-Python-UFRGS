""""Item 1 - Leia um número e imprima na tela o seu dobro se ele for menor do que 10. Se o número
for de 10 até 20, imprima a sua metade. Em qualquer outro caso, imprima na tela que o
número não é válido."""

#Entrada
num = int(input("Digite um número. "))

#Processamento e saída
if num<10:
    print(2*num)
elif num>=10 and num<=20:
    print(num/2)
else:
    print("O número não é válido.")
