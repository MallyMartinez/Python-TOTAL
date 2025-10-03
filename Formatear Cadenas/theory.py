"""
F O R M A T E A R  C A D E N A S 
    Para facilitar la concatenación de variables y texto,
    existen dos herramientas que evitan manipular las
    variables, para incorporarlas directamente al texto:

    Función format: 
    Se encierra las posiciones de las variables entre 
    corchetes { }, y a continuación del string llamamos a
    las variables con la función format.

    Cadenas literales (f-strings): 
    a partir de Python 3.8, podemos anticipar la 
    concatenación de variables anteponiendo f al string.

 """
x = 10
y = 5

"Conversioes y concatenaciónes (mal metodo)"
print ("Mis numeros son: " + str(x) + " y " + str(y))

"Función format"
print("Mis numeros son: {} y {}".format(x, y))
print("La suma de {} + {} es: {}".format(x, y, x+y))


"Cadenas literales (f-strings)"
color ="rojo"
matricula = "ABC123"

print(f'El carro es {color} y su matricula es {matricula}')