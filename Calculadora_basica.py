#!/usr/bin/env python
# coding: utf-8

# ## Aula 14/11 - Calculadora básica (Curso Extensão UFRGS)
# 
# Requisitos: Faça um programa de terminal que leia dois números digitados pelo usuário e a operação desejada entre (adição, subtração, multiplicação e divisão) e coloque o resultado na tela.
# 
# Autora: Tássia
# Data: 18/11/2022

# In[24]:


#Entrada

def escolha():
    print("\nDigite o número correspondente para escolher uma das seguintes operações matemáticas: \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")
    operacao = int(input("\nDigite um número de 1 a 4. "))
    if operacao <=0 or operacao > 4:
        print("\nO código é inválido")
    else:
        return operacao    


# In[25]:


##Entrada
#Definição da função entrada - usuário digita dois números.

def entrada():
    i=0
    numeros = []
    while i < 2:
        num = float(input("\nDigite um número. "))
        numeros.append(num)
        i += 1
    return numeros


# In[26]:


def main():
    opcao = escolha()
    numeros = entrada()
    if opcao == 1:
        resultado = numeros[0] + numeros[1]
    elif opcao == 2:
        resultado = numeros[0]-numeros[1]
    elif opcao == 3:
        resultado = numeros[0] * numeros[1]
    elif opcao == 4:
        if numeros[1] == 0:
            print("\nNão existe divisão por zero. ")
        else:
            resultado = numeros[0] / numeros[1]
    else:
        print("\nO código digitado é inválido. ")
    print(f"\nO resultado da operação é igual a {resultado}. ") 


# In[28]:


main()

