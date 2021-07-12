import random

tolerancia = 2

ingreso = int(input ("Ingrese una temperatura, ingrese 0 para salir: "))
while (ingreso<100 and ingreso>0 or ingreso>200):
	ingreso = int(input ("Error, reingrese temperatura entre 100º y 200º o 0 para salir: "))

while (ingreso != 0):

  objetivo = random.randint(100,200)

  suma=0

  for cantidad in range (10):
    suma = random.randint(objetivo-tolerancia,objetivo+tolerancia) + suma
  
  promedio = suma / 10.0

  if (promedio < ingreso-tolerancia):
    print("Temperatura baja, se enciende quemador")
  else:
    if (promedio > ingreso+tolerancia):
      print("Temperatura alta, se apaga quemador")
    else:
      print("Horno estable")
  print()

  ingreso = int(input ("Ingrese una temperatura, 0 para salir: "))
  while (ingreso<100 and ingreso>0 or ingreso>200):
	  ingreso = int(input ("Error, reingrese temperatura entre 100º y 200º o 0 para salir: "))

if (ingreso==0):
  print ("Cerrando programa")