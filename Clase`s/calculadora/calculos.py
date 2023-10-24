def suma(a,b):
    
    """
    Esta función nombraa 
    """
    
    return a + b

def resta(a, b):
    return a - b


def multiplicación(a, b):
    return a * b

def división(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return float(a/b)


def cuadrado(a):
    return a**2