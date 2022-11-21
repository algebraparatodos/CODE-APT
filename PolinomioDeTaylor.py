#Dada una función, obtener su polinomio de taylor.
#Para eso, necesitamos sus derivadas hasta orden "n"
#Evaluar la función y esas derivadas en "a".

import factorial as mipropiofactorial
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
x, y, z = symbols('x y z')

function=parse_expr(input("Ingrese la función (variables: x,y o z porfavor)"))
variable=input("¿Cuál es la variable?")
a=int(input("¿Cuál es el punto de centrado del polinomio?"))
n=int(input("¿De que orden desea el polinomio de taylor?"))

def Taylor(
    function,
    variable,
    a,
    n):
    
    if n<=0:
        return function.subs(variable,a)
    derivada=diff(function,variable,n)
    return (derivada.subs(variable,a)*(x-a)**n)/(mipropiofactorial.factorial(n)) + Taylor(function,variable,a,n-1)

print("El polinomio de Taylor de la función"+" "+str(function)+" es")

print(Taylor(function,variable,a,n))

print("--"*21)

