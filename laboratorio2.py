#!/usr/bin/python3
"""
Nombre: Ronny Granados Perez

El programa recibe nombres de entre 3 y 4 componentes en cualquier formato
(mayusculas, minusculas y combinacion de estas y las almacena; una vez que
se escriba SALIR, se devolveran los nombres almacenados con unicamente la
primera letra de cada palabra en mayuscula.

Ejemplo:

Entrada -> ronNy gRanaDos pereZ
Salida  -> Ronny Granados Perez

"""
# crear una lista para almacenar nombres
lista = []
flag = True
while (flag == True):
    full_name = input('Ingrese su nombre completo, o SALIR para salir: ')
    word_length = len(full_name.split(' '))
# establecer las condiciones bajo las que se manejara la entrada de nombres
    if (3 <= word_length <= 4):
        lista.append(full_name.title())
# definir el comando que permite salir
    elif (full_name == 'SALIR'):
        for i in lista:
            print('{}'.format(i))
            flag = False
# si no se ingresa un nombre de entre 3 y 4 palabras, habra un error
    else:
        print('Su entrada no es válida, intente de nuevo. \n')
