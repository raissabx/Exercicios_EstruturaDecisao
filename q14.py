nota1= float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2)/2

if media >= 9.0 and media <= 10.0:
    conceito = 'A'
    situacao = 'Aprovado'

elif media >= 7.5 and media < 9.0:
    conceito = 'B'
    situacao = 'Aprovado'
    
elif media >= 6.0 and media < 7.5:
    conceito = 'C'
    situacao = 'Aprovado'
    
elif media >= 4.0 and media < 6.0:
    conceito = 'D'
    situacao = 'Reprovado'

elif media < 4.0:
    conceito = 'E'
    situacao = 'Reprovado'
    
else:
    print('Tente novamente')


print(f'''
=======================
NOTAS
=======================
Nota 1: {nota1}
Nota 2: {nota2}
Média: {media}
Conceito: {conceito}
Situação: {situacao}
''')
