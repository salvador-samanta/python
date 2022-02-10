from Funciones.grafica import *
from Funciones.ejecucion_DB import *

conn = conexion()
cur = conn.cursor()

loop_active = True

while loop_active:
    borra()
    cabecera_busq_act()

    act_nomb = input ("Ingrese el nombre: ").capitalize().rstrip()
    act_ape = input ("Ingrese el apellido: ").capitalize().rstrip()

    confirm = input (f"Confirme el ingreso: \033[1;33m {act_nomb} {act_ape}\033[0;m s/n ")
    print()

    if confirm.upper() in ("S", "SI", "S", "SÍ"):
        ## buscar en la DB la ID del actor
        query_de_actor = cur.execute("select * from actores where UPPER(nombre_act) = :name and UPPER(apellido_act) = :lname",{"name":act_nomb.upper(), "lname":act_ape.upper()})
        actor_id =  query_de_actor.fetchone()

        
        if actor_id == None:
            print("\033[1;33m{} {} \033[0;m no se encuentra, intentalo de nuevo.".format(act_nomb, act_ape))
            input("Presione <enter>. ")
            continue

        actor_id = actor_id[0]

     #buscar películas con la ID del actor
        found_movies = cur.execute("""
           select
               peliculas.titulo_peli,
               peliculas.año_peli,
               director.nombre_dir,
               director.apellido_dir,
               pais.nombre_pais, 
               idioma.nombre_idioma,
               tematica.nombre_tema,
               prota1.nombre_act,
               prota1.apellido_act,
               prota2.nombre_act,
               prota2.apellido_act,
               peliculas.puntaje_peli
           from
               peliculas,
               director,
               pais,
               idioma,
               tematica,
               actores as prota1,
               actores as prota2
           where
               director.id_director = peliculas.dire_peli and
               pais.id_pais = peliculas.pais_peli and
               idioma.id_idioma = peliculas.idioma_peli and
               tematica.id_tema = peliculas.tematica_peli and
               prota1.id_actores = peliculas.prota1_peli and
                prota2.id_actores = peliculas.prota2_peli and
                (peliculas.prota1_peli = :actorid or peliculas.prota2_peli= :actorid)
           """, {"actorid": actor_id} )
    
        for movie in found_movies:
           nombre, anio, director_nom, director_ape, pais, idioma, tematica, prota_nom, prota_ape, prota2_nom, prota2_ape, puntaje = movie 
           print("Título: " + "\033[1;33m" + nombre + "\033[0;m" + " / Año: " + "\033[1;33m" + str(anio) + "\033[0;m")
           print("Director: " + "\033[1;33m" + director_nom, director_ape + "\033[0;m")
           print("Pais: "+ "\033[1;33m" + pais + "\033[0;m" + "/ Idioma: " + "\033[1;33m" + idioma + "\033[0;m")
           print("Genero: "+ "\033[1;33m" + tematica + "\033[0;m")
           print("Actores: " + "\033[1;33m" + prota_nom, prota_ape + ", " + prota2_nom, prota2_ape + "\033[0;m")
           print("Puntaje: " + "\033[1;33m" + str(puntaje) + "\033[0;m")
           print()

        seguir = input("Desea hacer otra búsqueda? s/n: ")
        if seguir.upper() in ("N", "NO"):
            print ("Adiós")
            loop_active = False
            conn.close()
