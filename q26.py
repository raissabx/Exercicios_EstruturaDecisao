from math import comb


combustivel = str(input('Qual combustível deseja? G-gasolina ou A-álcool: ')).upper()
litros = float(input('Quantos litros: '))
alcool = litros * 1.90
gasolina = litros * 2.50



if combustivel == 'A':
    if litros <= 20:
        desconto = alcool * 0.03
        total = alcool - desconto
        print(f'Total a pagar por {litros} litros R$: {round(total,2)}')
    
    elif litros > 20:
        desconto = alcool * 0.05
        total = alcool - desconto
        print(f'Total a pagar por {litros} litros R$: {round(total,2)}')

if combustivel == 'G':
    if litros <= 20:
        desconto = gasolina * 0.04
        total = gasolina - desconto
        print(f'Total a pagar por {litros} litros R$: {round(total,2)}')

    elif litros > 20:
        desconto = gasolina * 0.06
        total = gasolina - desconto
        print(f'Total a pagar por {litros} litros R$: {round(total,2)}')




