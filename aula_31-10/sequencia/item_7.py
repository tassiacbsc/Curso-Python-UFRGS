#Item 7 - Determine o n-ésimo termo e a soma dos termos de uma progressão geométrica.
#Entrada
n_pg = int(input("Digite o número de termos da PG. "))
n1_pg = int(input("Digite o primeiro termo da PG. "))
q = int(input("Digite o quociente da PG. "))
#Processamento
#determinar n-ésimo termo (fórmula termo geral da PG)
an_geo = n1_pg * q**(n_pg-1)
#soma dos termos da PG
somaPG = (n1_pg *(q**n_pg-1))/(q-1)
#Saída
print(an_geo)
print(somaPG)
