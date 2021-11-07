#!/usr/bin/python3

"""
- Ronny Granados Pérez

El usuario deberá indicar un número entero positivo
en la terminal que corresponderá a un índice
posicional en la secuencia de fibonacci, el programa
imprimirá el número correspondiente a esa posición.
Además, de manera opcional podrá obtener el tiempo
que le tomó al sistema procesar ese cálculo
y/o imprimir la secesión completa hasta esa posición.

"""

import argparse
import time

# Declaro el objeto ArgumentParser
parser = argparse.ArgumentParser()

parser.add_argument(
    'posicion',
    type=int,
    help='Posicion en la secuencia de Fibonacci que debe ser calculado.'
)
parser.add_argument(
    '--tiempo',
    '-t',
    action="store_true",
    help='Imprime el tiempo transcurrido para finalizar el cálculo.'
)
parser.add_argument(
    '--completa',
    '-c',
    action="store_true",
    help='Imprime la secuencia completa.'
)

# Obtengo los argumentos y los guardo en args
args = parser.parse_args()
# Cuenta el tiempo que dura en ejecutarse la funcion.
start = time.time()


def fibonacci(number):
    if (number == 0 or number == 1):
        solution = 1
    elif (number < 0):
        raise ValueError('Ingrese un valor entero positivo.')
    else:
        solution = fibonacci(number - 1) + fibonacci(number - 2)
    return solution


# Aca deja de tomar el tiempo y lo almacena en una variable
end = time.time()

# Variable donde se almacena el tiempo de ejecucion
timee = end - start

# condiciones para ejecutar en la terminal

# si solo se le da el parametro obligatorio
if args.tiempo is False and args.completa is False:
    print(
        'El número de fibonacci '
        'de índice {} es: {}'
        .format(args.posicion, fibonacci(args.posicion))
    )

# se da el numero y se pide la sucesion completa (-c, --completa)
if args.completa is True and args.tiempo is False:
    lista = range(args.posicion+1)
    print(
        'La serie de Fibonacci'
        ' hasta el índice {} es: '
        .format(args.posicion)
    )
    for i in lista:
        print('{}'.format(fibonacci(i)))

# se da el numero y pide el tiempo (-t, --tiempo)
if args.tiempo is True and args.completa is False:
    print(
        'El número de fibonacci '
        'de índice {} es: {}'
        .format(args.posicion, fibonacci(args.posicion))
    )
    print(
        'Tiempo total de ejecución: {}'
        .format(timee)
    )

# si se entregan el numero y -c y -t o viceversa
if args.completa is True and args.tiempo is True:
    # primero lo de la lista:
    lista = range(args.posicion+1)
    print(
        'La serie de Fibonacci '
        'hasta el índice {} es: '
        .format(args.posicion)
    )
    for i in lista:
        print(
            '{}'
            .format(fibonacci(i))
        )
    # luego lo del tiempo:
    print(
        'Tiempo total de ejecución: {} segundos.'
        .format(timee)
    )
