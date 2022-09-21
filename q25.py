ponto = int(0)

p1 = str(input('Telefonou para a vítima? S/N: ')).upper()
if p1 == 'S':
    ponto = ponto + 1
else: ponto = ponto + 0

p2 = str(input('Esteve no local do crime? S/N: ')).upper()
if p2 == 'S':
    ponto = ponto + 1
else: ponto = ponto + 0

p3 = str(input('Mora perto da vítima? S/N: ')).upper()
if p3 == 'S':
    ponto = ponto + 1  
else: ponto = ponto + 0

p4 = str(input('Devia para a vítima? S/N: ')).upper()
if p4 == 'S':
    ponto = ponto + 1   
else: ponto = ponto + 0

p5 = str(input('Já trabalhou com a vítima? S/N: ')).upper()
if p5 == 'S':
    ponto = ponto + 1 
else: ponto = ponto + 0    


if ponto == 2:
    print('Supeito')

elif ponto == 3 or ponto == 4:
    print('Cúmplice')

elif  ponto == 5:
    print('Assassino')

elif ponto == 0: 
    print('Inocente')