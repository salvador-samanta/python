from os import system
system ("cls")
from tabulate import tabulate
from Funciones.grafica import *
from Funciones.ejecucion_DB import *

save=[]

while True:
	con = conexion()
	cur = con.cursor()

	cabecera_busq_pelicula()

	nom_peli = input("Ingrese el nombre de la película: ").capitalize().rstrip()
	if nom_peli == '' or nom_peli.isnumeric() == True :
		input("\nAlgún valor no es válido. Presione <enter> para seguir.")    
		continue

	conf_ingreso = input("\nConfirme el ingreso '" + "\033[1;33m" + nom_peli + "\033[0;m" + "' (s/n): ")

	if conf_ingreso.lower()=="s":
		save.append(nom_peli)		
		sel= """SELECT titulo_peli, nombre_dir, apellido_dir, nombre_pais, nombre_idioma, nombre_tema, nombre_act, apellido_act, puntaje_peli, año_peli
            FROM peliculas, director, actores, idioma, tematica, pais 
            WHERE dire_peli=id_director and pais_peli=id_pais
            and idioma_peli=id_idioma and tematica_peli=id_tema 
            and prota1_peli=id_actores and titulo_peli = ?"""
		cur.execute(sel,(save))
		con.commit()
		fet = cur.fetchall()
		print()
		if fet == []:
			print("ATENCIÓN: NO EXISTEN PELÍCULAS CON ESE NOMBRE EXACTO")
			input("Presione <enter> para continuar.")
		else:
			print(tabulate(fet, headers=['Nombre de pelicula','Nombre Director','Apellido','País', 'Idioma', 'Temática', 'Nombre Actor','Apellido', 'Puntaje','Año'], tablefmt='fancy_grid'))
			input("Presione <enter> para continuar.")
		con.close()
		save.remove(nom_peli)
	print()
	nueva_busq=input("¿Desea hacer otra búsqueda (s/n): ")
	if nueva_busq.lower()!="s":
		break
