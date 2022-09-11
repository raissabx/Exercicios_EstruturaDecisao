'''Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

produto1 = float(input('Digite o valor do arroz: '))
produto2 = float(input('Digite o valor do feijão: '))
produto3 = float(input('Digite o valor do açúcar: '))

produtoMaisBarato = min(produto1, produto2, produto3)

if produtoMaisBarato == produto1:
    print ('O produto mais barato é o arroz')

elif produtoMaisBarato == produto2:
    print('O produto mais barato é o feijão')

else:
    print('O produto mais barato é o açúcar')