#Item 6 - Determine o n-ésimo termo e a soma dos termos de uma progressão aritmética.
#Entrada
n = int(input("Digite o número de termos da PA. "))
a1 = int(input("Digite o primeiro termo da PA. "))
r = int(input("Digite a razão da PA. "))
#Processamento
#determinar n-ésimo termo (fórmula termo geral da PA)
an = a1 + (n-1) * r
#soma dos termos da PA
somaPA = (a1 + an)*n/2
#Saída
print(an)
print(somaPA)
