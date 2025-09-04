"""
I N P U T
    Función que permite al usuario introducir información por
    medio del teclado al ejecutarse, otorgándole una instrucción
    acerca del ingreso solicitado. 

    El código continuará ejecutándose luego de que el usuario 
    realice la acción.
"""

#Opcion 1 simple
input("Dime tu nombre: ")
input("Dime tu apellido: ")

#Opcion 2 CON print
print(input("Dime tu nombre: "))

#Opcion 3 CON concatenacion
print("Tu nombre es " + input("Dime tu nombre: ") + " " + input("Dime tu apellido: "))
