'''Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
qtd = 3

for i in range(qtd):
    numero = int(input('Digite um número: '))
    lista.append(numero)

lista.sort(reverse=True)
print(lista)'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

if n1 != maior and n1 != menor:
    meio = n1
elif n2 != maior and n2 != menor:
    meio = n2

elif n3 != maior and n3 != menor:
    meio = n3

print(menor, meio, maior, sep=',')


