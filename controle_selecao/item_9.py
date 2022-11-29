 """Item 9 - Leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal (IMC), classifique
essa pessoa de acordo com a tabela abaixo e escreva na tela a condição da pessoa:"""

peso = float(input("Digite seu peso. "))
altura = float(input("Digite sua altura. "))
imc = peso/altura**2
if imc<18.5:
    print("excessivamente magro")
elif imc>18.5 and imc<=25:
    print("peso normal")
elif imc>25 and imc<=30:
    print("sobrepeso")
else:
    print("obeso")
