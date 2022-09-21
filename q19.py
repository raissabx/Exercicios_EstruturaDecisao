numero = int(input('Digite um número inteiro: '))

unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(centena)

print(f'centena {centena}, dezena {dezena} e unidade {unidade}')