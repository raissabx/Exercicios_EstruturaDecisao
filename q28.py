print('='* 23)
print('Hipermercado Tabajara'.upper())
print('='* 23)
print('Promoções de até 5 Kg:')
print('''File Duplo      R$ 4,90 por Kg  
Alcatra         R$ 5,90 por Kg 
Picanha         R$ 6,90 por Kg ''')
print('-'* 30)
print('Promoções acima de 5 Kg:')
print('''File Duplo      R$ 5,80 por Kg  
Alcatra         R$ 6,80 por Kg 
Picanha         R$ 7,80 por Kg''')

carne = input('Digite qual carne você quer: ').lower()
quilos = float(input('Quantos quilos irá comprar: '))
cartao = input('Possui Cartão Tabajara? S/N: ').upper()
total = 0
desconto = 0

if carne == 'file duplo':
    if quilos <= 5:
        total = float(quilos * 4.90)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

    if quilos > 5:
        total = float(quilos * 5.80)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

if carne == 'alcatra':
    if quilos <= 5:
        total = float(quilos * 5.90)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

    if quilos > 5:
        total = float(quilos * 6.80)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

if carne == 'picanha':
    if quilos <= 5:
        total = float(quilos * 6.90)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

    if quilos > 5:
        total = float(quilos * 7.80)
        if cartao == 'S':
            desconto = float(total * 0.05)
            total = float(total - desconto)
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')
        elif cartao == 'N':
            print('-'* 20)
            print('CUMPOM FICAL')
            print('-'* 20)
            print(f'File Duplo -----> {quilos} Kg = {round(total,2)}')

            





