from Funciones.grafica import busqueda_anio
from Funciones.ejecucion_DB import *

while True:
    busqueda_anio()
    opcion = input("\n\tSeleccione opción: ") 
    if opcion == "1":
        while True:
            busqueda_anio()
            try:
                v_anio = int(input("Buscar películas por año de estreno (1900 a 2021): "))
                if 1900 <= v_anio <= 2021:
                    break
                else:
                    input("\nEl Año no está en el rango solicitado. Presione <ENTER>.")
                    continue
            except:
                input("Ingrese un dato válido. Presione <ENTER>.")

        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, año_peli 
                FROM peliculas, tematica WHERE año_peli = {}
                AND tematica_peli == id_tema;""".format(v_anio)

        seguir = buscar(seleccion, "Año")
        if seguir == 'c': continue
        elif seguir == 'b': break

    elif opcion == "2":
        while True:
            busqueda_anio()
            try:
                v_anio = int(input("Buscar películas que se estrenaron antes del Año que indique (1900 a 2021): "))
                if 1900 <= v_anio <= 2021:
                    break
                else:
                    input("\nAño no válido. Presione <ENTER>.")
                    continue
            except:
                s()
                input("Ingrese un dato válido. \nPresione <ENTER>.")

        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, año_peli 
                    FROM peliculas, tematica WHERE año_peli < {}
                    AND tematica_peli = id_tema ORDER BY año_peli;""".format(v_anio)
        seguir = buscar(seleccion, "Año")
        if seguir == 'c': continue
        elif seguir == 'b': break
        
    if opcion == "3":
        while True:
            busqueda_anio()
            try:
                print("Buscar películas entre un rango de Años (entre 'A1' y 'A2'):\n")
                anio_minimo = int(input("Indique año inicial 'A1' (1900 a 2021): "))
                anio_maximo = int(input("Indique año final 'A2' (1900 a 2021): "))
                s()
                if 1900 <= anio_minimo <= 2021 and 1900 <= anio_maximo <= 2021 and anio_minimo<anio_maximo :
                    break
                else:
                    s()
                    input("El Año no está en el rango solicitado o 'A1' es mayor o igual a 'A2' \nPresione <ENTER>.")
                    continue
            except:
                input("Ingrese un dato válido. \nPresione <ENTER>.")
                
        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, año_peli 
                    FROM peliculas, tematica WHERE año_peli BETWEEN {} AND {}
                    AND tematica_peli == id_tema ORDER BY año_peli;""".format(anio_minimo, anio_maximo)
        seguir = buscar(seleccion, "Año")
        if seguir == 'c': continue
        elif seguir == 'b': break
        
    elif opcion == "4":
        while True:
            busqueda_anio()
            try:
                v_anio = int(input("Buscar películas que se estrenaron después del Año que indique (1900 a 2021): "))
                if 1900 <= v_anio <= 2021:
                    break
                else:
                    input("\nAño no válido. Presione <ENTER>.")
                    continue
            except:
                s()
                input("Ingrese un dato válido. \nPresione <ENTER>.")

        seleccion = """SELECT id_peli, titulo_peli, nombre_tema, año_peli 
                    FROM peliculas, tematica WHERE año_peli > {}
                    AND tematica_peli = id_tema ORDER BY año_peli;""".format(v_anio)
        seguir = buscar(seleccion, "Año")
        if seguir == 'c': continue
        elif seguir == 'b': break
                
    elif opcion.upper() == "S":
        break
    else:
        input("\nOpción no válida. Presione <ENTER>. ")
