"""
C O N V E R S I O N E S
    El proceso de convertir un tipo de dato en otro tipo de dato 
    se llama el casting, y existen dos tipos:

    implícitas: 
        Realiza conversiones implícitas de tipos de datos
        automáticamente para operar con valores numéricos. 

    explícitas:
        Se necesita al usuario para realize la conversion
        de un tipo de dato a otro. 

"""

"Conversiones implícitas"
num1 =20
num2 =30.5

num1 = num1 + num2 

print(type(num1))
print(type(num2)) 


"Conversiones explícitas"
num3 =5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))


edad = input("¿Cual es tu edad? ")
edad = int(edad)
print(type(edad))

nueva_edad = edad + 1
print("El proximo año tendras: ", nueva_edad)

