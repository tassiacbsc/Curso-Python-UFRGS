""""Item 10 - dado o número de horas trabalhadas por um empregado de uma empresa que paga R$
20,00 por hora trabalhada e desconta imposto de renda (ir) segundo a tabela abaixo,
determine o salário líquido do empregado."""

horas_trabalho = int(input("Digite a quantidade de horas trabalhadas. "))
s_bruto = horas_trabalho*20
print(f"O salário bruto é R$ {s_bruto}.")
if s_bruto<=1000:
    print(f"O salário líquido é R$ {s_bruto}.")
elif s_bruto>1000 and s_bruto<=2500:
    print(f"O salário líquido é R$ {0.9*s_bruto}.")
elif s_bruto>2500 and s_bruto<=5000:
    print(f"O salário líquido é R$ {0.8*s_bruto}.")
else:
    print(f"O salário líquido é R$ {0.65*s_bruto}.")
