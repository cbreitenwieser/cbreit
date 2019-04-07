resultado = int(input('Pense em dois números de 0 a 9, multiplique o primeiro numero por 2, some 3 ao resultado e multiple por cinco depois e some o segundo numero:'))
print(resultado) #valor inserido
numeros = str(resultado - 15)
print (numeros) #valor para calcular os numeros
x = len(numeros) #lenght
for char in numeros: #para cada caractere no nome
    print ('numero: ',char) #imprima o caractere
