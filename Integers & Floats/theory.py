
"""
I N T E G E R  &  F L O A T S 
    Existen dos tipos de datos numéricos básicos en Python: int y
    float. Como toda variable en Python, su tipo queda definido al
    asignarle un valor a una variable. 

"""

""" 
    Int, o integer, es un número entero, positivo o negativo, sin
    decimales, de un largo indeterminado.
"""

mi_numero = 1 + 3
print(mi_numero + mi_numero)


"""
La función type() nos permite
obtener el tipo de valor almacenado en una variable
"""
print(type(mi_numero))


"""     
    Float, o "número de punto flotante" es un número que puede
    ser positivo o negativo, que a su vez contiene una o más
    posiciones decimales.
"""
mi_numero = 5.8 + 5
mi_numero = mi_numero + mi_numero
print(mi_numero)

print(type(mi_numero))



edad = input("Dime tu edad: ")
print("Tu edad es " + edad)

print(type(edad))

"""
Esto no es valido ya que si deseamos hacer la suma 
nos marcara error al querer juntar un int con un string
    nueva_edad = 1 + edad
    print ("Vas a cumplir "+ nueva_edad)
"""
