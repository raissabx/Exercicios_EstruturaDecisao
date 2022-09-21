nota1 = float(input('Dpuigite a primeira nota: '))
nota2 = float(input('Dpuigite a segunda nota: '))
nota3 = float(input('Dpuigite a terceira nota: '))
media = (nota1 + nota2 + nota3)/3

if media >= 7 and media < 10:
    print(f'Aprovado com média {media}')

elif media < 7:
    print(f'Reprovado com média {media}')

elif media == 10:
    print(f'Aprovado com Distinção com média {media}')