fruit_1=input("¿Cuál es tu fruta preferida?")
fruit_2=input("¿y cuál es tu segunda fruta preferida?")

fruit_list=[
    fruit_1,
    fruit_2
]

answer_1=input("Creo que sería delicioso un budín de"+" "+fruit_list[0]+"\
 y "+fruit_list[1]+",¿no lo crees?")

if answer_1 == "no":
    print("¿Cómo que no?, estas loco")
else:
    print("Creo que seremos buenos amigos")
