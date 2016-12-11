def inversa(n):
    if n==0:
        print "inicia cuenta regresiva"
    else:
        print n
        inversa(n-1)
        
        
def factorialN(n):
    if n ==0:
        return 1
    else:
        return n * factorialN(n-1)
        
        
def fibo(n):
    a,b=0,1
    while b < n:
        print b,
        a,b=b,a+b