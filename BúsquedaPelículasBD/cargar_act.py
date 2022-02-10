from Funciones.grafica import *
from Funciones.ejecucion_DB import *

conn = conexion()
cur = conn.cursor()


while True:
    borra()
    cabecera_act()
    
    #pedimos los datos a agregar utilizando el capitalize para dejar el ingreso con la primera 
    #letra en mayusculas como esta en la base de datos
    apellido = input("Ingrese Apellido del Actor: ").capitalize().rstrip()
    nombre = input("Ingrese Nombre del Actor : ").capitalize().rstrip()
    if apellido == '' or nombre == '' or apellido.isnumeric() == True or nombre.isnumeric() == True :
        input("\nAlgún valor no es válido. Presione <enter> para seguir.")
        continue
        
    seguir = carga_actor_si_existe(apellido, nombre)
    if seguir == 'no seguir': 
        continue
    elif seguir == 'salir':
        break 

    pais = input("\nIngrese País de nacimiento, para saber el código del país: ").capitalize().rstrip()
    if pais == '':
        input("\nIngreso no válido. Presione <enter>.")
        continue

    # Buscamos si existe el pais y mostramos los codigos.
    seguir = carga_pais_si_existe(pais, 'pais', 'id_pais', 'nombre_pais')
    if seguir == 'no seguir': 
        input("\nPresione <enter> para volver a cargar el Actor o Actríz.")
        continue
       
    #con el comando insert or ignore insertamos los datos solo si no estan en la base
    insertar ='''INSERT INTO actores (nombre_act, apellido_act, pais_act) VALUES(?, ?, ?)'''
    cur.execute(insertar, (nombre, apellido, seguir)) 
    conn.commit()

    borra()
    cabecera_act()
    print("\n\033[1;33m Actor o Actríz agregado correctamente. \033[0;m")
    if (input("\n¿Desea Cargar otro Actor o Actríz? s / n : ")).upper() =="N":
        break
    else:
        pass  

conn.close()
