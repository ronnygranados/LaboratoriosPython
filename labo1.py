#!/usr/bin/python3

datovalido = True
while (datovalido == True):
  try:
    iterador = int(input("Ingrese el valor para el iterador: "))
    if iterador <= 0:
      print("Ingrese un valor de iterador mayor que cero. \n")
    else:
      datovalido = False
  except:
    print("El iterador solo admite números enteros positivos \n")

char = input("Ingrese un caracter para constuir la pirámide: ")

for n in range(1,iterador+1):
  print(char*n)

