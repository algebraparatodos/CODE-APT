#Este programa es para aprender a utilizar listas
#Una lista se construye utlizando corchetes
#Ejemplo de lista lista_1=[elemento_0,elemento_1,elemento_2]
#Para recuperar un elemento, utilizo números de 0 a n (izquierda a derecha)
#Tambíen pueden recuperarse de derecha a izquierda utilizando números negativos
#Ejemplo: lista_1=[elemento_-3,elemento_-2,elemento_-1]

print("Mi lista de frutas preferidas es")

lista_frutas=[
    "banana",
    "manzana",
    "pera",
    "sandia",
    "manzana",
    "kiwi",
    "piña"
]

print(lista_frutas)

print("De todas ellas, hoy comí solo"+" "+lista_frutas[2])

print("--"*30)
#El resultado es equivalente si escribimos print("De todas ellas, hoy comí solo"+" "+lista_frutas[-5])

print("De todas ellas, hoy comí solo"+" "+lista_frutas[-5])

