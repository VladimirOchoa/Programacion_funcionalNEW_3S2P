import calculadora.calculos as calc

print(calc.suma.__doc__)
print(calc.suma(2, 3))


#----------------------------------------------------------------

from calculadora import calculos

print(calc.suma(2,3))
print(calc.resta(2,3))
print(calc.resta(2,3))
print(calc.división(2,3))

#-----------------------------------------------------------------


from calculadora.calculos import suma

print(suma(2,3))

#-----------------------------------------------------------------

from calculadora.calculos import*

print(suma(2,3))
print(resta(2,3))
print(multiplicación(2,3))
print(división(2,3))

#-----------------------------------------------------------------

from calculadora.calculos import suma as sumar

print(sumar(2,3))