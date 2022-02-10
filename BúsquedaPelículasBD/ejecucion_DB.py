from Funciones.grafica import *
import sqlite3
import pathlib
from tabulate import tabulate

# funcion que retorna la ruta del archivo 'Proyecto_Movies'
def ruta_base():
    ruta = str(pathlib.Path(__file__).parent.absolute())
    ruta=ruta[:-9]
    return ruta

# funcion para establecer conexion a la BD. Retorna la conexion.
def conexion():
    #ruta = ruta_base()
    conexion = sqlite3.connect(ruta_base() + "BaseDeDatos/movies.db")
    return conexion

# ejecuta o abre otro archivo .py
def ejecutar(archivo):
    exec(open(ruta_base() + archivo, encoding='utf-8').read())

           
def director_si_existe(dato, tabla, campo1, campo2):
    borra()
    cabecera_busq_director()
    conn = conexion()
    cur = conn.cursor()
    # si la tabla tiene 2 campos entra al 'if'
    existe = "SELECT {}, {} FROM {};".format(campo1, campo2, tabla)
   
    cur.execute(existe)
    conn.commit()
    lista = cur.fetchall()
    conn.close()

    lista_id = []  # nos guarda las coincidencias.
    conteo = 0  # contamos cuantas coincidencias encuentra.
    
    print("'" + "\033[1;33m" + dato + "\033[0;m" + "' no se encuentra en la Base de Datos.\n")
    
    for dato1, dato2 in lista:
        if dato1[0:4] == dato[0:4]:
            print("\033[1;33m" + dato1 + "\033[0;m", dato2)
            lista_id.append(id)
            conteo += 1

    # encontro al menos 1 campo con las 4 primeras letras iguals
    # ingresa al 'if' y pregunta que hacemos con ese valor.
    if conteo != 0:
        print("\nSe encontró " + str(conteo) + " datos similares en la Base de Datos.")
        input("Presione <enter> para seguir.")
    else:
        input("\nPresione <enter> para seguir.")

def carga_actor_si_existe(ape, nom):
    borra()
    cabecera_act()
    conn = conexion()
    cur = conn.cursor()
    # si la tabla tiene 2 campos entra al 'if'
    existe = """SELECT apellido_act, nombre_act FROM actores 
            WHERE apellido_act = \'{}\' AND nombre_act = \'{}\';""".format(ape, nom)
   
    cur.execute(existe)
    conn.commit()
    lista = cur.fetchall()
    conn.close()

    lista_id = []  # nos guarda las coincidencias.
    conteo = 0  # contamos cuantas coincidencias encuentra.

    for a, n in lista:
        if a[0:4] == ape[0:4] and n[0:4] == nom[0:4]:
            print(a, n)
            lista_id.append(id)
            conteo += 1

    # encontro al menos 1 campo con las 4 primeras letras iguals
    # ingresa al 'if' y pregunta que hacemos con ese valor.
    if conteo != 0:
        volver = input("\nEl Director ya existe en la Base de Datos. \n¿Desea cargar otro Director? s / n : ")
        if volver.upper() == 'S':
            return 'no seguir'
        else:
            return 'salir'
        
    else:
        print("'" + "\033[1;33m" + ape, nom + "\033[0;m" + "' se cargará en la Base de Datos.")
        return 'seguir'

def carga_director_si_existe(ape, nom):
    borra()
    cabecera_dire()
    conn = conexion()
    cur = conn.cursor()
    # si la tabla tiene 2 campos entra al 'if'
    existe = """SELECT apellido_dir, nombre_dir FROM director 
            WHERE apellido_dir = \'{}\' AND nombre_dir = \'{}\';""".format(ape, nom)
   
    cur.execute(existe)
    conn.commit()
    lista = cur.fetchall()
    conn.close()

    lista_id = []  # nos guarda las coincidencias.
    conteo = 0  # contamos cuantas coincidencias encuentra.

    for a, n in lista:
        if a[0:4] == ape[0:4] and n[0:4] == nom[0:4]:
            print(a, n)
            lista_id.append(id)
            conteo += 1

    # encontro al menos 1 campo con las 4 primeras letras iguals
    # ingresa al 'if' y pregunta que hacemos con ese valor.
    if conteo != 0:
        volver = input("\nEl Director ya existe en la Base de Datos. \n¿Desea cargar otro Director? s / n : ")
        if volver.upper() == 'S':
            return 'no seguir'
        else:
            return 'salir'
            
    else:
        print("'" + "\033[1;33m" + ape, nom + "\033[0;m" + "' se cargará en la Base de Datos.")
        return 'seguir'

    
def carga_pais_si_existe(dato, tabla, campo1, campo2):
    borra()
    # Esta funcion se usa desde cargar_act.py y cargar_dir.py
    if tabla == 'actores':
        cabecera_act()
    elif tabla == 'director':
        cabecera_dire()
    else:
        cabecera_pais()
        
    conn = conexion()
    cur = conn.cursor()
    
    existe = "SELECT {}, {} FROM {};".format(campo1, campo2, tabla)
   
    cur.execute(existe)
    conn.commit()
    lista = cur.fetchall()
    conn.close()

    lista_id = []  # nos guarda las coincidencias.
    conteo = 0  # contamos cuantas coincidencias encuentra.

    for id, dato1 in lista:
        if dato1[0] == dato[0]:
            print(id, dato1)
            lista_id.append(id)
            conteo += 1

    # encontro al menos 1 campo con las 4 primeras letras iguals
    # ingresa al 'if' y pregunta que hacemos con ese valor.
    if conteo != 0:
        try:
            pais = int(input("\nIndique número de país si se encuentra en la lista, sino 0: "))
            # si no hay registro en la BD, le pedimos que vaya a 'Cargar Pais'
            if pais == 0:
                print()
                print("\033[1;33m" + dato + "\033[0;m", "no se encontró en la Base de Datos.")
                input("\nPresione <enter> para realizar la carga.")
                ejecutar("cargar_pais.py")
                return 'no seguir'
            else:
                return pais
        except:
            input("Valor no válido. \nPrecione <enter> para continuar.")
            return 'no seguir'   
    else:
        print("\033[1;33m" + dato + "\033[0;m", "no se encontró en la Base de Datos.")
        input("\nPresione <enter> para realizar la carga.")
        ejecutar("cargar_pais.py")
        return 'no seguir'

# muestra la tabla 'pais' de 2 campos.
def mostrar_tabla(tabla, campo):
    conn = conexion()
    cur = conn.cursor()
    insertar = "SELECT * FROM {} ORDER BY {};".format(tabla, campo)
    cur.execute(insertar)
    conn.commit()
    lista_tabla = cur.fetchall()
    conn.close()
    # pasamos la lista de la DB para que se imprima y ordene en columnas.
    mostrar_en_columnas(lista_tabla)


# funcion para ordenar e imprimir listas en 2 o 3 columnas.    
def mostrar_en_columnas(lista):
    x = 0
    elementos = len(lista[0])
    # ordena e imprime una lista de 2 elementos en 3 columnas
    if elementos == 2:
        for id, dato in lista:
            print(str(id).ljust(3), dato.ljust(21), end='')
            x += 1 
            if x == 3:
                print()
                x = 0
    # ordena e imprime una lista de 3 elementos en 2 columnas
    elif elementos == 3:
        for id, dato1, dato2 in lista:
            cadena = dato1 + ' ' + dato2
            print(str(id).ljust(3), cadena.ljust(30), end='')
            x += 1 
            if x == 2:
                print()
                x = 0
    # ordena e imprime una lista de 3 elementos en 2 columnas
    elif elementos == 4:
        for id, dato1, dato2, dato3 in lista:
            print(str(id).ljust(3), dato1.ljust(45), dato2.ljust(25), str(dato3).ljust(4))
    # ordena e imprime una lista de 3 elementos en 2 columnas
    elif elementos == 5:
        for dato1, dato2, dato3, dato4, dato5 in lista:
            print(dato1.ljust(45), dato2.ljust(17), dato3.ljust(17), str(dato4).ljust(6), str(dato5).ljust(4))

def cambiar_numeros(lista):
    conn = conexion()
    cur = conn.cursor()
    
    seleccionar = ["SELECT nombre_dir, apellido_dir FROM director WHERE id_director = {};",
                "SELECT nombre_pais FROM pais WHERE id_pais = {};",
                "SELECT nombre_idioma FROM idioma WHERE id_idioma = {};",
                "SELECT nombre_tema FROM tematica WHERE id_tema = {};",
                "SELECT nombre_act, apellido_act FROM actores WHERE id_actores = {};",
                "SELECT nombre_act, apellido_act FROM actores WHERE id_actores = {};"]
    j = 1
    lista_cambio = []
    for i in seleccionar:
        sel = i.format(lista[j])
        j += 1            
        cur.execute(sel)
        conn.commit()
        dato = list(cur.fetchone())
        lista_cambio.append(dato)
    conn.close()
    return lista_cambio

def cargar_pelicula(lista):
    # print(lista)
    conn =conexion()
    cur = conn.cursor()

    insertar = """INSERT INTO peliculas VALUES(
        NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    cur.execute(insertar, lista)
    conn.commit()
    conn.close()

def bt(tematica):
    conn = conexion()
    cur = conn.cursor()
    seleccion= ''' SELECT titulo_peli, nombre_dir, apellido_dir, nombre_pais, nombre_act, apellido_act, puntaje_peli, año_peli 
        FROM peliculas, director, pais, tematica, actores 
        WHERE dire_peli=id_director and pais_peli=id_pais and tematica_peli=id_tema and prota1_peli=id_actores and nombre_tema="{}" '''.format(tematica)
    
    cur.execute(seleccion)
    conn.commit()
    b= cur.fetchall()
    #mostramos en pantalla las opciones seleccionadas con el comando tabulate para que se muestre ordenada
    print(tabulate(b, headers=['Nombre de pelicula','Nombre Director','Apellido','Pais','Nombre de Actor','Apellido','Puntaje IMDB','Año'], tablefmt='fancy_grid'))


def buscar(sel, anio_imdb):
    conn = conexion()
    cur = conn.cursor()
    cur.execute(sel)
    conn.commit()
    datos = cur.fetchall()
    conn.close()
        
    # Si la lista esta vacia, no hay registros en la DB con esa busqueda.
    if datos == []:
        print("\nNo se encontraron registros en su busqueda.")  
    else:
        s()
        # Imprimimos la cabecera de las columnas
        print("\033[1;33m" + "ID".ljust(3), "Titulo Película".ljust(45), 
                "Temática".ljust(25), anio_imdb.ljust(4) + "\033[0;m")
        mostrar_en_columnas(datos)
            
    if input("\n¿Desea continuar buscando por " + anio_imdb + "? s / n : ").upper() == 'S':
        return 'c'
    else:
        return 'b'

# funcion para carga_peli.py    
def carga_peli_buscar(archivo, dato, tabla, id_campo, campo1, campo2):
    seguir = si_existe(dato, tabla, id_campo, campo1, campo2)
    if seguir == 'c': 
        print("\033[1;33m" + dato + "\033[0;m", "no se encontró en la Base de Datos.")
        input("\nPresione <enter> para realizar la carga.")
        # si no existe en la BD, cargamos el dato llamando al archivo enviado.
        ejecutar(archivo)
        # una vez q cargo el dato en la tabla correspondiente. 
        # vuelve a pedir que lo busquemos.
        return 'c'
    elif seguir == 'n':
        return 'c'
    else:
        return seguir

# Funcion para 'Cargar Pelicula', evalua si existe el valor en la tabla especificada.
def si_existe(dato, tabla, id_campo, campo1, campo2):
    borra()
    cabecera_peli()
    conn = conexion()
    cur = conn.cursor()
    # si la tabla tiene 2 campos entra al 'if'
    if campo2 == None:
        existe = "SELECT {}, {} FROM {};".format(id_campo, campo1, tabla)
    # si la tabla tiene 3 campos entra al 'else'
    else:
        existe = "SELECT {}, {}, {} FROM {};".format(id_campo, campo1, campo2, tabla)
    cur.execute(existe)
    conn.commit()
    lista = cur.fetchall()
    conn.close()

    lista_id = []  # nos guarda las coincidencias.
    conteo = 0  # contamos cuantas coincidencias encuentra.

    # si la tabla a mostrar tiene 2 campos entra al 'if'
    if campo2 == None:
        if tabla == 'pais':
            # solo en pais compara con la primer letra
            for id, dato1 in lista:
                if dato1[0] == dato[0]:
                    print(id, dato1)
                    lista_id.append(id)
                    conteo += 1
        else:    
            # compara las primeras 4 letras.
            for id, dato1 in lista:
                if dato1[0:4] == dato[0:4]:
                    print(id, dato1)
                    lista_id.append(id)
                    conteo += 1
    # si la tabla tiene 3 campos entra al 'else'
    else:
        for id, dato1, dato2 in lista:
            # si hay dos campos que comienzan con la 4 primeras 
            # letras iguales, las imprime: 
            if dato1[0:4] == dato[0:4]:
                print(id, dato1, dato2)
                # cada encuentro de coincidencia lo vamos juntando 
                # en una lista que nos va servir para validar que
                # que indique numero correcto. 
                lista_id.append(id)
                conteo += 1
    # encontro al menos 1 campo con las 4 primeras letras iguals
    # ingresa al 'if' y pregunta que hacemos con ese valor.
    if conteo != 0:
        # pregunta para la tabla pelicula.
        if tabla == 'peliculas':
            s()
            existe = input("Si '" + "\033[1;33m" + dato + "\033[0;m" + "' ya se encuentra en la Base de Datos, \nindique" +
                           " 'n' para cargar otra pelicula o 'c' para agregarla: ")
        # pregunta para las demas tablas.
        else:
            s()
            existe = input("Si '" + "\033[1;33m" + dato + "\033[0;m" + "' no se encuentra en la Base de Datos, \nindique" + 
                           " 'c' para cargarlo, sino el número que corresponda: ")
        if existe == 'c':
            # retorna que cargue el valor en una variable.
            return 'c'
        elif existe == 'n':
            # retorna que no cargue el valor.
            return 'n'
        else:
            try:
                if int(existe) not in lista_id:
                    input("Numero no válido.")
                    return 'n'
                else:
                    # retorna un numero para los campos con Foreign Keys.
                    existe = int(existe)
                    return existe
            except:
                input("Valor no válido.")
                # retorna que no cargue el valor.
                return 'n'
    # si no existe ningun valor que coincida en las primeras 4 letras. 
    # retorna que cargue la pelicula automaticamente.
    else:
        return 'c'
 
