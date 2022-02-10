from Funciones.grafica import *
from Funciones.ejecucion_DB import *

#Realizamos la conexion con la base de datos
conn = conexion()
cur = conn.cursor()
cabecera_pais()

#hacemos un while para el ingreso
while True:
	#pedimos el pais a agregar utilizando el capitalize para dejar el ingreso con la primera 
	#letra en mayusculas como esta en la base de datos
	pais= input("Ingrese Nuevo Pais: ").capitalize().rstrip()
	confirm = input("Confirme el ingreso: " + "\033[1;33m" + pais.capitalize().rstrip() + "\033[0;m" + " (s/n): ")

	if pais.isnumeric() == True:
		print("Solo se aceptan letras")
		continue	

	#con el comando insert or ignore insertamos el pais solo si no esta en la base
	a=" INSERT OR IGNORE INTO pais (nombre_pais) VALUES (?) "
	cur.execute(a, [pais])
	conn.commit()
	print("Pais Agregado Correctamente")
	if (input("¿Desea Cargar Otro Pais? s / n :")).upper() =="N":
		break
	else:
		pass
#cerramos la conn con la base de datos	
conn.close()			
