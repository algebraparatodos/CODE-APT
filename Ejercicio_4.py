from sympy import *

print("Vamos a ver si sabes sumar")

value_1=input("Ingresa un número: ")

value_2=input("Ahora, ingresa otro número: ")

sum_1=int(value_1)+int(value_2)

print("Tómate un momento para calcular la suma")

answer_1=input("¿Estás listo? (si/no): ")

if answer_1 == "si":
    print("la suma es "+str(sum_1))
    answer_2=input("¿Qué tal ha ido? (bien/mal): ")
    if answer_2 == "bien":
        print("¡Buen trabajo!")
    else:
        print("¡Vuelve a intentarlo!")
elif answer_1 == "no":
    print("Pues mala suerte, aquí va la respuesta")
    print("la suma es"+str(answer_1))
else:
    print("respuesta incorrecta, comienza de nuevo")

print("--"*22)

#Vamos a intentarlo con una función

print("Vamos a ver si sabes sumar")

value_1=input("Ingresa un número: ")

value_2=input("Ahora, ingresa otro número: ")

def addition(
    value_1,
    value_2):

    return int(value_1)+int(value_2)

print("La suma es "+str(addition(value_1,value_2)))

