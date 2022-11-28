"""Programa calculadora_basica
Requisitos: Faça um programa de terminal que leia dois números
digitados pelo usuário e a operação desejada entre (adição,
subtração, multiplicação e divisão) e coloque o resultado na
tela.
Autor: Tássia
Data: 28/11/2022

"""

# Importação de módulos

import view


def main():
       
    # processamento
    print("\nDigite o número correspondente para escolher uma das seguintes operações matemáticas: \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")
    operacao = int(input("\nDigite um número de 1 a 4. "))
    
    numeros = view.entrada()

    if operacao == 1:
        resultado = numeros[0] + numeros[1]
    elif operacao == 2:
        resultado = numeros[0]-numeros[1]
    elif operacao == 3:
        resultado = numeros[0] * numeros[1]
    elif operacao == 4:
        resultado = numeros[0] / numeros[1]
    else:
        print("\nCódigo digitado é inválido. ")

    # saida
    view.saida(resultado)

if __name__ == "__main__":
    main()
