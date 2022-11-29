# Item 6 - leia um texto e informe se ele é o nome da capital de um estado da região sul do Brasil.

capital_sul = ['Curitiba','Florianópolis','Porto Alegre']
capital = input("Digite o nome de uma capital do Brasil. ")
if capital in capital_sul:
    print(f"{capital} é uma capital do Sul do Brasil.")
    
