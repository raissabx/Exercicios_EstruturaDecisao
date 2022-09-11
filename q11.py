'''As Organizações Tabajara resolveram dar um aumento de salário aos seus
 colaboradores e lhe contraram para desenvolver o programa que calculará os 
 reajustes. Faça um programa que recebe o salário de um colaborador e o 
 reajuste segundo o seguinte critério, baseado no salário atual:

*salários até R$ 280,00 (incluindo) : aumento de 20%
*salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
*salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
*salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser 
realizado, informe na tela:
    *o salário antes do reajuste;
    *o percentual de aumento aplicado;
    *o valor do aumento;
    *o novo salário, após o aumento.'''

salario = float(input('Digite o valor do seu salário atual: R$ '))

if salario <= 280:
    calculo = (salario * 0.2)
    novoSalario = calculo + salario
    percentual = ('20%')

elif salario > 280 and salario < 700:
    calculo = (salario * 0.15)
    novoSalario = calculo + salario
    percentual = ('15%')

elif salario > 700 and salario < 1500:
    calculo = (salario * 0.1)
    novoSalario = calculo + salario
    percentual = ('10%')

elif salario > 1500:
    calculo = (salario * 0.05)
    novoSalario = calculo + salario
    percentual = ('5%')
    
    #print('Seu novo salário será de: R$ ', novoSalario)

print('Seu salário atual é de: R$ ', salario)
print('O percentual aplicado será de: ', percentual)
print('O valor do aumento será de: R$ ', calculo)
print('O valor do seu novo salário é de: R$ ', novoSalario)

