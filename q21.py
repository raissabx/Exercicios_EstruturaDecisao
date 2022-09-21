from socket import NI_NUMERICHOST


saque = int(input('Digite o valor que deseja sacar: '))

cem = saque // 100
saque = saque - (cem * 100)

cinquenta = saque // 50
saque = saque - (cinquenta * 50)

vinte = saque // 20
saque = saque - (vinte * 20)

dez = saque // 10
saque = saque - (dez * 10)

cinco = saque // 5
saque = saque - (cinco * 5)

um = saque

print(f'Notas de R$ 100: {cem}')
print(f'Notas de R$ 50: {cinquenta}')
print(f'Notas de R$ 20: {vinte}')
print(f'Notas de R$ 10: {dez}')
print(f'Notas de R$ 5: {cinco}')
print(f'Notas de R$ 1: {um}')
