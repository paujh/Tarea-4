#Jorge Hinostrosa Paula 
#Tarea 4. 
#Haremos un programa que calcule las medidas de dispersion de los numeros de una lista.
from math import sqrt

#Media. 
def media(l):
  n = len(l)
  suma = 0.0
  for i in l:
    suma = suma + i
  return  suma/n

#Varianza.
def varianza(l):
  prom = media(l)
  n = len(l)
  suma = 0.0
  for i in l:
    suma = suma + (i-prom)**2.0
  return suma/n

#Desviacion estandar
def desvEst(l):
  return sqrt(varianza(l))

#Mediana (metodo sort para ordenar listas)
def mediana(l):
  n = len(l)
  l.sort()
  if n%2==1:
    return l[n//2]
  else:
    return (l[n//2] + l[(n//2)-1])/2.0

#Moda
def moda(l):
  d = {}
  for i in l:
    if i in d:
      d[i] = d[i] + 1
    else:
      d[i] = 1
  maxRep = 0
  eleMasRep = l[0]
  for i in d:
    if d[i] > maxRep:
      maxRep = d[i]
      eleMasRep = i
  if len(d) != len(l):
    return eleMasRep
  else:
    return ("No hay moda")    


#Haremos una prueba de las formulas
l1 = [0.05, 0.0632, 1.2, 5.35, 7.45, 1.098, 1.234, 4.562, 1.543, 0.076, 2.865, 0.654, 5.961, 4.632, 2.316, 8.521, 5.862, 4.21, 0.542, 2.864]
print(media(l1))
print(varianza(l1))
print(desvEst(l1))
print(mediana(l1))
print(moda(l1))
