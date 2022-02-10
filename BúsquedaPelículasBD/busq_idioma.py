from Funciones.grafica import *
from Funciones.ejecucion_DB import *
from tabulate import tabulate

con=conexion()

cur=con.cursor()

while True:
	borra()
	cabecera_idioma()	
	opcion = input("\nBÚSQUEDA POR IDIOMA \n\nIngrese una opción: ")

	if opcion == "1":
	    aleman= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Alemán"'''
	    cur.execute(aleman)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")
	    
	elif opcion == "2":
	    arabe= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Árabe"'''
	    cur.execute(arabe)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "3":
	    chino= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Chino"'''
	    cur.execute(chino)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "4":
	    español= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Español"'''
	    cur.execute(español)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "5":
	    frances= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Francés"'''
	    cur.execute(frances)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "6":
	    griego= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Griego"'''
	    cur.execute(griego)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))

	elif opcion == "7":
	    ingles= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Inglés"'''
	    cur.execute(ingles)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "8":
	    italiano= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Italiano"'''
	    cur.execute(italiano)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "9":
	    japones= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Japonés"'''
	    cur.execute(japones)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "10":
	    polaco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Polaco"'''
	    cur.execute(polaco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "11":
	    portugues= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Portugués"'''
	    cur.execute(portugues)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "12":
	    ruso= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Ruso"'''
	    cur.execute(ruso)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "13":
	    coreano= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Coreano"'''
	    cur.execute(coreano)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "14":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Sueco"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")
     
	elif opcion == "15":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Bengalí"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "16":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Hindú"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "17":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Indonesio"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "18":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Persa iraní"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "19":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Tailandés"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "20":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Turco"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion == "21":
	    sueco= ''' SELECT titulo_peli, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
            FROM peliculas, director, pais, idioma, tematica, actores 
            WHERE dire_peli=id_director and pais_peli=id_pais and idioma_peli=id_idioma and tematica_peli=id_tema and prota1_peli=id_actores 
            and nombre_idioma="Vietnamita"'''
	    cur.execute(sueco)
	    con.commit()
	    lista= cur.fetchall()
	    print(tabulate(lista, headers=['Nombre de pelicula','Nombre Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))
	    input("Presione <enter> para continuar.")

	elif opcion.upper() =="S":
		break
	elif (input ("\nOpción incorrecta. Desea realizar una nueva búsqueda?:  s/n ").upper() =="N"): 
		break
		
con.close()
