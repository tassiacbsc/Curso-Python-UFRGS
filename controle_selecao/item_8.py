"""Item 8 - solicite as notas de um aluno nas avaliações previstas no plano de ensino desta disciplina,
calcule a sua média e informe se o aluno está aprovado ou reprovado com base nas notas
obtidas, incluindo a recuperação. Use este programa para avaliar seu próprio desempenho
na disciplina."""

#Entrada
cont=0
soma = 0
while cont<4:
    nota = float(input("Digite a sua nota. "))
    soma = soma + nota
    cont+=1
media = soma/4
if media<5:
    print("Você está reprovado")
elif media>=5 and media<6:
    print("Você está de recuperação")
else:
    print("Você está aprovado")
