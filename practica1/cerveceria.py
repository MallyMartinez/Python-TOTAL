"""
Practica 1: cerveceria
    Tu mejor amigo ha puesto una fábrica de cerveza y tiene todo listo.
    Su producto es fantástico, tiene cuerpo, buen sabor, buen color, 
    el nivel justo de espuma.Pero le falta una identidad.

    No se le ocurre qué nombre ponerle su cerveza para que tenga 
    una identidad única y original.

*   Entonces, vas a crear un programa que te va a hacer dos preguntas 
*   y luego te va a decir cuál es el nombre de tu cerveza, 
*   para formar una marca creativa.

    Así de simple. Ya sé que en el mundo real no necesitaríamos desarrollar 
    un software solo para hacer dos preguntas,pero hasta que aprendamos más 
    funcionalidades, bueno, los programas van a tener que mantenerse en
    el terreno de lo simple.
"""
uno = input("Escribe lo primero que se te venga a la mente: ")
dos = input("Escribe lo segundo que se te venga a la mente: ")
print('Tu cerveza se llama \n"' + uno + ' ' + dos + '"')


#? Ejemplo del curso 
#1ro paso
print("El nombre de tu cerveceria es 'palabra1 palabra2'")

#2do paso
print("El nombre de tu cerveceria es '" + palabra1 + " " + palabra2 + "'")

#3ro paso
print("El nombre de tu cerveceria es '" + input("Que ciudad te gustaria visitar?: ") + " " + palabra2 + "'")

#4to paso
print("El nombre de tu cerveceria es '" + input("Que ciudad te gustaria visitar?: ") 
      + " " + input("Cual es tu color favorito?: ") + "'")

#Paso final
print("El nombre de tu cerveza\nes '" + input("Que ciudad te gustaria visitar?: ") 
     + " " + input("Cual es tu color favorito?: ") + "'\nFelicitaciones!")