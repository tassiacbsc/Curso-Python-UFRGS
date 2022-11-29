#Item 3 - leia cinco números e imprima na tela o quadrado de cada um deles.

i = 0
while i<5:
    n = int(input("Digite um número e será apresentado o valor dele ao quadrado. "))
    print(n**2)
    i = i + 1
    if i==5:
        break
