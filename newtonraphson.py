print("Vamos a usar una función")

def NewtonRaphson(initial_solution,exponent,independent_term):
    x=initial_solution
    n=0
    while abs(pow(x,exponent)-independent_term) > 0.000001:
        #Fórmula es: x_n+1=x_n-f(x_n)/f´(x_n)
        x = x - (pow(x,exponent)-independent_term)/(exponent*pow(x,exponent-1))
        n = n + 1
    return x



