#Item 5 - Imprima na tela os 10 primeiros termos de uma progressão aritmética cuja razão é dada
#pelo usuário.
razao = float(input("Digite a razão da progressão aritmética. "))
n1 = float(input("Digite o primeiro termo da progressão aritmética. "))
n10 = n1+ (10-1)*razao
i=n1
while n1<=n10:
    print(n1)
    n1 = n1+razao
