from Funciones.grafica import *
from Funciones.ejecucion_DB import *

#hacemos un while para el ingreso
while True:
	
	borra()
	#ya que son pocos items colocamos un menu para facil acceso
	busqueda_tematica()
	
	#realizamos el input para la seleccion de la opcion controlando errores
	
	try:
		opcion = int(input("Ingrese un Numero de Genero: "))
	except(ValueError):
		print("Por Favor Ingrese solo Numeros")
		input()
		continue

	#corremos un IF para las opciones de menu
	if opcion == 0:
		break
	elif opcion == 1:
		#realizamos la verificacion de toda la informacion que queremos mostrar
		bt("Accion")		
		input()
	elif opcion == 2:
		bt("Aventura")
		input()	
	elif opcion == 3:
		bt("Ciencia Ficcion")
		input()
	elif opcion == 4:
		bt("Comedia")
		input()
	elif opcion == 5:
		bt("Crimen")
		input()
	elif opcion == 6:
		bt("Drama")
		input()
	elif opcion == 7:
		bt("Fantasia")
		input()
	elif opcion == 8:
		bt("Romantica")
		input()
	elif opcion == 9:
		bt("Suspenso")
		input()
	elif opcion == 10:
		bt("Thriller")
		input()
	else:
		print("Opcion Inexistente Seleccione Nuevamente \t")
