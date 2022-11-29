""" Item 2 - Leia um número e imprima na tela a mensagem ”O número é par.”se o número lido for
par e ”O número é impar” se o número lido for ímpar. Em caso de número não inteiros 
ou negativos, imprima na tela ”Este número não é válido.” """

num = float(input("Digite um número. "))
if num<0:
    print("Este número não é válido")
else:
    if (num%2) == 0:
        print("O número é par")
    elif (num%2) ==1:
        print("O número é ímpar")
    else:
        print("O número não é válido")
