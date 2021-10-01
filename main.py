from functions import gcd, egcd, modInverse, testFermat,binpow, generator

#a= 1036,b= 240;•a= 22896,b= 192;•a= 689161,b= 378851.
print('\n GDC Euclids Algorithm')
print(gcd(1036,240))
print(gcd(22896,192))
print(gcd(689161,378851))

#•a= 1036,b= 240;•a= 8753,b= 3354;•a= 2021,b= 43.
print('\n Extended Euclids Algorithm')
print(egcd(1036,240))
print(egcd(8753,3354))
print(egcd(2021,43))

print('\n Mod Inverse')
#•a= 47,n= 2020;•a= 31,b= 1234;•a= 65,b= 17316.
print(modInverse(47,2020))
print(modInverse(31,1234))
print(modInverse(65,17316))

print('\n Fermat test')
#FALTA COMPARAR CON EL VALOR DE LA TABLA DE PRIMOS PARA COMPROBAR EFICACIA
#1317,2709,3257,3911,4279,5497,6311,7223,8431,9203.
teoricos = [3257, 3911, 6311, 8431, 9203]
numeros = [1317, 2709, 3257, 3911, 4279, 5497, 6311, 7223, 8431, 9203]
print(testFermat(1317,5))
print(testFermat(2709,5))
print(testFermat(3257,5))
print(testFermat(3911,5))
print(testFermat(4279,5))
print(testFermat(5497,5))
print(testFermat(6311,5))
print(testFermat(7223,5))
print(testFermat(8431,5))
print(testFermat(9203,5))

for x in numeros:
    if (x in teoricos):
        print(str(x) + " teoricamente, es un numero primo")


#Generador
print('\n Generator of primes with Fermat')
longitud = int(input('Ingrese la longitud de los numeros primos: '))
cantidad = int(input('Ingrese la cantidad de primos a generar: '))


print(generator(longitud,cantidad))