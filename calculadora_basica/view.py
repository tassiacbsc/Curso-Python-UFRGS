"""Módulo view.py
Requisito: Este módulo agrega as funções de entrada e saída de dados
Autor: Tássia
Data: 28/11/2022
"""


def entrada():
    """Esta função lê o teclado da calculadora."""
    i=0
    numeros = []
    while i < 2:
        num = float(input("\nDigite um número. "))
        numeros.append(num)
        i += 1
    return numeros


def saida(resultado):
    """Esta função escreve na tela do usuário o resultado
    da operação realizada na calculadora."""
    print(f"\nO resultado é igual a {resultado}.")
