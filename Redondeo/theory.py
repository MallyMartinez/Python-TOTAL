"""
R E D O N D E O
    Facilita la interpretación de los valores 
    calculados al limitar la cantidad de 
    decimales que se muestran en pantalla.
    También, nos permite aproximar valores 
    decimales al entero más próximo.

"""
print(90/7)


"Directamente"
print(round(90/7))


"Con variable"
resultado = 90/7
print(round(resultado))


"Con decimales"
print(round(resultado, 2))


"Tipo de dato"
valor =round(95.66666666666)
print(valor)
print(type(valor))

valor1 = 95.66666666666
print(round(valor1))
print(type(valor1))