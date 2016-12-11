def imprimeDoble(paso):
    print paso,paso


def catDoble(parte1, parte2):
    cat= parte1 * parte2
    imprimeDoble(cat)
    
    
def funcion(x):
    if x >3:
        return x * x * x
    else: 
         print 'X es menor que 3'
         
def calculo_iva(valor, iva=0.13):
    return valor * iva                 
    
def maximo(d,f,g):
    maximo = max(d,f,g)
    print maximo   