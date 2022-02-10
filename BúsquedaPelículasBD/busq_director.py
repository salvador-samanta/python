from Funciones.grafica import *
from Funciones.ejecucion_DB import *

conn = conexion()
cur = conn.cursor()

while True:
    borra()
    cabecera_busq_director()

    try:
        apellido = input("Ingrese el Apellido: ")
        s()
        conf_ingreso = input("Confirme el ingreso: " + "\033[1;33m" + apellido.capitalize().rstrip() + "\033[0;m" + " (s/n): ")
    except:
        continue
        
    if conf_ingreso.lower()=="s":
        # en {} hay agregarle las comillas, para que lo tome como calor str, 
        # sino lo toma como una columna '= Spielberg'. Bien -> '= "Spielberg"'
        seleccionar= '''SELECT titulo_peli, nombre_tema, nombre_pais,
            puntaje_peli, año_peli 
            FROM peliculas, director, pais, tematica 
            WHERE dire_peli = id_director AND pais_peli = id_pais  
            AND tematica_peli = id_tema  
            AND apellido_dir = \"{}\";'''.format(apellido)
        cur.execute(seleccionar)
        conn.commit()
        datos = cur.fetchall()
           
        # Si la lista esta vacia, no hay registros en la DB con esa busqueda.
        if datos == []:
            print("\nLista de Directores con apellidos similares: ")
            director_si_existe(apellido.capitalize(), 'director', 'apellido_dir', 'nombre_dir')
            continue         
        else:
            s()
            # Imprimimos la cabecera de las columnas
            print("\033[1;33m" + "Titulo Película".ljust(45), 
                  "Temática".ljust(17), "País".ljust(17), 
                  "IMDB".ljust(6), "Año".ljust(4) + "\033[0;m")
            mostrar_en_columnas(datos)

        if input("\nDesea continuar buscando por Director? s / n : ").upper() == 'S':
            continue
        else:
            conn.close()
            break
    else:
        continue
