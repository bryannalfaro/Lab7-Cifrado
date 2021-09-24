#https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
#https://www.techiedelight.com/extended-euclidean-algorithm-implementation/
#https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
#Algoritmos de clase


import numpy as np
def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def egcd(a, b):
    xp  = 0
    yp = 1
    if a == 0:
        return b, xp, yp
    else:
        gcd, x, y = egcd(b % a, a)
        xp = y - (b // a) * x
        yp = x
        return gcd,xp, yp


def modInverse(a,n):

    g,x,y =egcd(a,n)
    if(g!=1):
        return 'No existe inverso'
    else:
        res = x%n
        return res

def testFermat(n,k):
    prime = True
    pruebas = []
    for i in range(0,k):
        a = np.random.randint(2,n-2)
        pruebas.append(a)
        if (binpow(a,n-1)%n)!=1:
            prime = False
    if prime:
        return prime,pruebas
    else:
        return prime,a

#https://cp-algorithms.com/algebra/binary-exp.html
def binpow(a,b):
    if b==0:
        return 1
    result = binpow(a,b//2)
    if b % 2:
        return result * result *a
    else:
        return result*result

def generator(longitud, cantidad):
    numb = '1'+(longitud-1)*'0'
    numb = int(numb)
    print(numb)
    print(numb*100)
    primos = []
    while len(primos) < 5:
        numero = np.random.randint(numb, numb*100)
        if testFermat(numero,5)[0]==True:
            print('Se genero un primo ')
            primos.append(numero)
        else:
            pass

    return primos