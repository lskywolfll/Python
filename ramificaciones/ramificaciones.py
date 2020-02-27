
contador = 2
primerNumero = int(input('Ingresa tu primer numero: \n'))

if primerNumero >= 0:
    contador -= 1
    print(f'Te queda {contador} numero faltante')

segundoNumero = int(input('Ingresa tu segundo numero: \n'))

if segundoNumero >= 0:
    contador -= 1
    print(f'Te queda {contador} numero faltante')

if primerNumero > segundoNumero:
    print(f'El numero {primerNumero} es mayor que el numero{segundoNumero}')
elif primerNumero == segundoNumero:
    print(f'Los numeros son iguales!! 🤯')
else:
    print(f'El numero {segundoNumero} es mayor que el {primerNumero}')
