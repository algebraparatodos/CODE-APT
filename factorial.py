from cgi import print_arguments
from math import factorial

def factorial(numero):
    factor=numero
    total=1
    while(factor>1):
        total=total*factor
        factor=factor-1
    return total

