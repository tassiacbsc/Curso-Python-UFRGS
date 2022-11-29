"""Item 4 - Leia o nome e a idade de uma pessoa. Se a pessoa tiver menos de 18 anos, imprimir
”[nome] não pode assistir a este filme.” onde no lugar de [nome] deve sair o nome lido do
teclado."""

nome = input("\nDigite o seu nome. ")
idade = int(input("\nDigite a sua idade. "))
if idade<18:
    print(f"{nome} não pode assistir a este filme.")
    
