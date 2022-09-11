from cmath import sin


valorHora = float(input('Digite o valor da sua hora: R$ '))
horasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas neste mês: '))

salarioBruto = valorHora * horasTrabalhadas
sindicato = salarioBruto * 0.03
fgts = salarioBruto * 0.11
ir = 0
inss = salarioBruto * 0.1
totalDescontos = 0


if salarioBruto <= 900:
    ir = 0
    totalDescontos = inss + sindicato

elif salarioBruto > 900 and salarioBruto <= 1500:
    ir = (salarioBruto * 0.05)
    totalDescontos = ir + inss + sindicato

elif salarioBruto > 1500 and salarioBruto <= 2500:
    ir = (salarioBruto * 0.1)
    totalDescontos = ir + inss + sindicato

elif salarioBruto > 2500:
    ir = (salarioBruto * 0.2)
    totalDescontos = ir + inss + sindicato

salarioLiquido = salarioBruto - totalDescontos

print('Seu salário bruto é de: R$ ', salarioBruto)
print('O desconto de IR é de: R$ ', ir)
print('O desconto de INSS é de: R$ ', inss)
print('O desconto de FGTS é de: R$ ', fgts)
print('O desconto de Sindicato é de: R$ ', sindicato)
print('O total de descontos é de: R$ ', totalDescontos)
print('Seu salário líquido é de: R$ ',salarioLiquido)



