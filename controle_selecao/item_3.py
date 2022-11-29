"""Item 3 -  Leia um número, determine se ele é múltiplo de 3 e imprima na tela a mensagem ”Este
número é múltiplo de 3”ou ”Este número não é múltiplo de 3”a depender do caso."""

num = int(input("Digite um número. "))
if (num%3)==0:
    print("Este número é múltiplo de 3")
else:
    print("Este número não é múltiplo de 3")
