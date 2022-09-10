'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra 
escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input('Digite F - Feminino, M - Masculino: ')

if sexo == 'F' or sexo == 'f':
    print('Feminino')

elif sexo.lower() == 'm':
    print('Masculino')

else:
    print('Sexo Inválido')


#print('Feminino' if sexo == "F" elif sexo == "M" else "" )