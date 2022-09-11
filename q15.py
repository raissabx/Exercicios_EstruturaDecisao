l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))

if l1 == l2 == l3:
    print('Triangulo Equilátero')

elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Triângulo Isósceles')

elif l1 != l2 != l3:
    print('Triângulo Escaleno')

