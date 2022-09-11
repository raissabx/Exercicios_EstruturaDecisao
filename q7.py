'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maiorNum = max(n1, n2, n3)
menorNum = min(n1, n2, n3)

print('O maior número é o ', maiorNum)
print('O menor número é o ', menorNum)
