from Funciones.grafica import busqueda_puntaje, finaliza
from Funciones.ejecucion_DB import *


while True:
    busqueda_puntaje()
    opcion = input("\n\tSeleccione opción: ") 
    if opcion == "1":
        while True:
            busqueda_puntaje()
            try:
                puntaje = int(input("Buscar películas que tengan el siguiente puntaje (0 a 9): "))
                if 0 <= puntaje <= 9:
                    break
                else:
                    input("\nEl número no está en el rango solicitado. Presione <ENTER>.")
                    continue
            except:
                input("Ingrese un dato válido. Presione <ENTER>.")
        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, puntaje_peli 
                    FROM peliculas, tematica WHERE puntaje_peli BETWEEN {} AND {}.9
                    AND tematica_peli == id_tema;""".format(puntaje, puntaje)
        seguir = buscar(seleccion, "IMDB")
        if seguir == 'c': continue
        elif seguir == 'b': break

    elif opcion == "2":
        while True:
            busqueda_puntaje()
            try:
                puntaje = float(input("Buscar películas que tengan un puntaje menor o igual a (0.0 a 9.9): "))
                if 0.0 <= puntaje <= 9.9:
                    break
                else:
                    input("\nNúmero no válido. Presione <ENTER>.")
                    continue
            except:
                s()
                input("Ingrese un dato válido. El número decimal es con '.' (punto).\nPresione <ENTER>.")

        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, puntaje_peli 
                    FROM peliculas, tematica WHERE puntaje_peli < {}
                    AND tematica_peli = id_tema ORDER BY puntaje_peli;""".format(puntaje)

        seguir = buscar(seleccion, "IMDB")
        if seguir == 'c': continue
        elif seguir == 'b': break

    if opcion == "3":
        while True:
            busqueda_puntaje()
            try:
                print("Buscar películas entre dos puntajes 'P1' y 'P2':\n")
                puntaje_minimo = float(input("Indique puntaje mínimo 'P1' (0.0 a 9.9): "))
                puntaje_maximo = float(input("Indique puntaje máximo 'P2' (0.0 a 9.9): "))
                s()
                if 0 <= puntaje_minimo <= 9.9 and 0 <= puntaje_maximo <= 9.9 and puntaje_minimo<puntaje_maximo :
                    break
                else:
                    s()
                    input("El número no está en el rango solicitado o 'P1' es mayor o igual a 'P2' \nPresione <ENTER>.")
                    continue
            except:
                input("Ingrese un dato válido. El número decimal es con '.' (punto).\nPresione <ENTER>.")
                
        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, puntaje_peli 
                    FROM peliculas, tematica WHERE puntaje_peli BETWEEN {} AND {}
                    AND tematica_peli == id_tema ORDER BY puntaje_peli;""".format(puntaje_minimo, puntaje_maximo)

        seguir = buscar(seleccion, "IMDB")
        if seguir == 'c': continue
        elif seguir == 'b': break

    elif opcion == "4":
        while True:
            busqueda_puntaje()
            try:
                puntaje = float(input("Buscar películas que tengan un puntaje mayor o igual a (0.0 a 9.9): "))
                if 0.0 <= puntaje <= 9.9:
                    break
                else:
                    s()
                    input("El número no está en el rango solicitado. Presione <ENTER>.")
                    continue
            except:
                s()
                input("Ingrese un dato válido. El número decimal es con '.'\nPresione <ENTER>.")

        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, puntaje_peli 
                    FROM peliculas, tematica WHERE puntaje_peli > {}
                    AND tematica_peli = id_tema ORDER BY puntaje_peli;""".format(puntaje)

        seguir = buscar(seleccion, "IMDB")
        if seguir == 'c': continue
        elif seguir == 'b': break
                
    elif opcion.upper() == "S":
        break
    else:
        input("\nOpción no válida. Presione <ENTER>. ")
