numero = int(input('Digite um numero: '))
resultado = ''

if numero == 0:
    resultado = 'zero'
elif numero < 0:
    resultado = 'negativo'
else:
    resultado = 'positivo'


print(f'o numero {numero} é {resultado}')
