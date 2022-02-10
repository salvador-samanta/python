from os import *
from Funciones.grafica import borra, s, cabecera_peli
from Funciones.ejecucion_DB import *


borra()

# Carga Pelicula.
while True:
    # Ingreso Pelicula
    while True:
        cabecera_peli()
        s()
        pelicula = input("Ingrese Título de la Película: ")
        if pelicula == '': continue
        
        # buscamos si existe la pelicula.
        seguir = si_existe(pelicula, 'peliculas', 'id_peli', 'titulo_peli', None)
        if seguir == 'c':
            # carga la variable con la pelicula y continua con Ingreso Director.
            titulo_peli = pelicula
            break
        elif seguir == 'n':
            # vuelve a pedir una pelicula.
            continue
    
    # Ingreso Director
    while True:
        borra()
        cabecera_peli()

        dire_peli = input("Apellido del Director: ")
        if dire_peli == '': continue
                
        hacer = carga_peli_buscar("cargar_dir.py", dire_peli.capitalize(), 'director', 'id_director', 'apellido_dir', 'nombre_dir')
        # si se ingreso un valor invalido, vuelve a pedir el Director.
        if hacer == 'c': continue
        else:
            # Si todo se ingreso bien, guardamos el id actores.
            dire_peli = hacer 
            break         
    
    # Ingreso Prota1
    while True:
        borra()
        cabecera_peli()

        prota1_peli = input("Apellido Actor o Actriz principal: ")
        if prota1_peli == '': continue
                
        hacer = carga_peli_buscar("cargar_act.py", prota1_peli.capitalize(), 'actores', 'id_actores', 'apellido_act', 'nombre_act')
        # si se ingreso un valor invalido, vuelve a pedir el Director.
        if hacer == 'c': continue
        else:
            # Si todo se ingreso bien, guardamos el id actores.
            prota1_peli = hacer 
            break         

    # Ingreso Prota2
    while True:
        borra()
        cabecera_peli()

        prota2_peli = input("Apellido Actor o Actriz secundario: ")
        if prota2_peli == '': continue
                
        hacer = carga_peli_buscar("cargar_act.py", prota2_peli.capitalize(), 'actores', 'id_actores', 'apellido_act', 'nombre_act')
        if hacer == 'c': continue
        else:
            prota2_peli = hacer 
            break         
    
    # Ingreso Pais
    while True:
        borra()
        cabecera_peli()

        pais_peli = input("Pais de producción: ")
        if pais_peli == '': continue
        
        hacer = carga_peli_buscar("cargar_pais.py", pais_peli.capitalize(), 'pais', 'id_pais', 'nombre_pais', None)
        if hacer == 'c': continue
        else:
            pais_peli = hacer 
            break         


    # Ingreso idioma
    s()
    while True:
        borra()
        cabecera_peli()

        mostrar_tabla('idioma','nombre_idioma')
        s()
        try:
            s()
            idioma_peli = int(input("Indique Idioma: "))
        except:
            input("Valor no válido.")    
            continue
        if 0 < idioma_peli < 22:
            break 
        
    # Ingreso Tematica
    s()
    while True:
        borra()
        cabecera_peli()

        mostrar_tabla('tematica','nombre_tema')
        s()
        try:
            s()
            tematica_peli = int(input("Indique Temática: "))
        except:
            input("Valor no válido.")    
            continue
        if 0 < tematica_peli < 11:
            break   
    
    # Ingreso puntaje
    s()
    while True:
        borra()
        cabecera_peli()

        try:
            puntaje_peli = input("Ingrese Puntaje: ")
            puntaje_peli = float(puntaje_peli)
        except:
            # por si usa coma en vez de punto.
            if ',' in puntaje_peli:
                input("Usar '.' (punto) para números decimales.")
                continue
            else:
                input("Valor no válido.")    
                continue
        if 0 <= puntaje_peli <= 10:
            break
 
    # Ingreso Año
    s()
    while True:
        borra()
        cabecera_peli()

        try:
            año_peli = int(input("Ingrese Año: "))
        except:
            input("Valor no válido.")    
            continue
        if 1900 <= año_peli <= 2021:
            break   
        else:
            input("Valor no válido.")
            continue
    
    # esta lista guardo la pelicula, con todos sus id de cada campo
    # se va a usar oara guardar los datos en la tabla 'peliculas'
    lista_pelicula = [titulo_peli, dire_peli, pais_peli, 
                      idioma_peli, tematica_peli, prota1_peli, 
                      prota2_peli, puntaje_peli, año_peli]    
 
    # Esta funcion retorna la lista con los nombres de cada campo 
    # ejemplo, cambia el id_pais '7' por la cadena 'EEUU'. 
    lista_cambios = cambiar_numeros(lista_pelicula)

    borra()
    cabecera_peli()
    # antes de guardas los datos los imprimimos para confirmarlos.
    print("Título de la Película: " + "\033[1;33m" + lista_pelicula[0] + "\033[0;m")
    print("Nombre del Director: " + "\033[1;33m" + lista_cambios[0][0] + " " + lista_cambios[0][1] + "\033[0;m")
    print("País de la Película: " + "\033[1;33m" + lista_cambios[1][0] + "\033[0;m")
    print("Idioma: " + "\033[1;33m" + lista_cambios[2][0] + "\033[0;m")
    print("Temática: " + "\033[1;33m" + lista_cambios[3][0] + "\033[0;m")
    print("Nombre Actor principal: " + "\033[1;33m" + lista_cambios[4][0] + " " + lista_cambios[4][1] + "\033[0;m")
    print("Nombre Actor secundario: " + "\033[1;33m" + lista_cambios[5][0] + " " + lista_cambios[5][1] + "\033[0;m")
    print("Puntaje IMDB: " + "\033[1;33m" + str(lista_pelicula[7]) + "\033[0;m")
    print("Año de la Película: " + "\033[1;33m" + str(lista_pelicula[8]) + "\033[0;m")
    s()
    
    # lista_pelicula = ["Rambo", 2, 8, 7, 1, 9, 12, 8.2, 1984]     
    if input("Desea cargar la película en la Base de Datos? s / n : ").upper() == "S":
        # hacemos la carga en la tabla 'peliculas'
        cargar_pelicula(lista_pelicula)
        print("Finalizo Carga.")
        s()
        if input("Desea cargar otra peliculas? s / n: ").upper() == "S":
            continue
        else:
            break
