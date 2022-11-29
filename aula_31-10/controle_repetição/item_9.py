#Item 9 - leia 6 números e imprima o cubo e a raiz cúbica de cada um deles.
cont = 0
while cont<6:
    num = int(input("Digite um número"))
    print(f"\nO cubo do número {num} é {num**3} e a raiz cúbica dele é {num**1/3}")
    cont = cont +1
    if cont==7:
        break
        
