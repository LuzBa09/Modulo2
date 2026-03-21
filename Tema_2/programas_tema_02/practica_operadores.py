def comparar_longitud(palabra1, palabra2):
    long_palabra1 = len(palabra1)
    long_palabra2 = len(palabra2)
    return long_palabra1 == long_palabra2
p1="gato"
p2="perro"
long_palabras=comparar_longitud(p1,p2)
print(f"¿Son '{p1}' y '{p2}' dos palabras con la misma longitud? {long_palabras} ")