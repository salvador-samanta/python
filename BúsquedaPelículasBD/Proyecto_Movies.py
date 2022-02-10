from Funciones.grafica import borra, menu_inicio, finaliza
from Funciones.ejecucion_DB import ejecutar
from os import system    

# Establece medida de la ventana de la terminal
system('mode con: cols=160 lines=45')

borra()

while True:
    opcion = menu_inicio()

    if opcion == "1":
        ejecutar("busq_peliculas.py")
    elif opcion == "2":
        ejecutar("busq_director.py")
    elif opcion == "3":
        ejecutar("busq_actores.py")
    elif opcion == "4":
        ejecutar("busq_tematica.py")
    elif opcion == "5":
        ejecutar("busq_puntaje.py")
    elif opcion == "6":
        ejecutar("busq_anio.py")
    elif opcion == "7":
        ejecutar("busq_idioma.py")
    elif opcion == "8":
        ejecutar("cargar_dir.py")
    elif opcion == "9":
        ejecutar("cargar_act.py")
    elif opcion == "10":
        ejecutar("cargar_pais.py")
    elif opcion == "11":
        # ejecutar("prueba.py")
        ejecutar("cargar_peli.py")
    elif opcion.upper() == "S":
        break
    else:
        input("Opción no válida. Presione <ENTER>. ")
finaliza()
