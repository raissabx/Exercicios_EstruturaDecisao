# ax2 + bx + c
# delta = b² - 4ac

import math
a = int(input('Digite o valor de A: '))

if a == 0:
    print('A igual a 0 não é permitido em equações do segundo grau! Programa encerrado!')
    exit()

else:    
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        print('Delta menor que 0. ')
    
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta = 0, raiz = {raiz}')

    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raizes: {raiz1} e {raiz2}')


