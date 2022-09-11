nota1= int(input('Digite o valor da primeira nota: '))
nota2 = int(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2)/2

if media >= 9.0 and media <= 10.0:
    print('Sua média foi de: ', media)
    print('Nota Conceito A')
    print('Aprovado')

elif media >= 7.5 and media < 9.0:
    print('Sua média foi de: ', media)
    print('Nota Conceito B')
    print('Aprovado')

elif media >= 6.0 and media < 7.5:
    print('Sua média foi de: ', media)
    print('Nota Conceito C')
    print('Aprovado')

elif media >= 4.0 and media < 6.0:
    print('Sua média foi de: ', media)
    print('Nota Conceito D')
    print('Reprovado')

elif media < 4.0:
    print('Sua média foi de: ', media)
    print('Nota Conceito E')
    print('Reprovado')

else:
    print('Tente novamente')