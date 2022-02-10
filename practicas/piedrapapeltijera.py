import random

aleatorio = random.randrange(0, 2)
respuestaPc = ""
resultado = ""
consigna = int(input("Ingresa el numero que elijas: 1)Piedra 2)Papel 3)Tijera"))

if consigna == 1:
	respuestaUsuario = "piedra"
elif consigna == 2:
	respuestaUsuario = "papel"
elif  consigna == 1:
	respuestaUsuario = "piedra"
else:
	respuestaUsuario = "un número equivocado!"

print ("Elegiste ", respuestaUsuario)

if aleatorio == 0:
	respuestaPc = "piedra"
elif aleatorio == 1:
	respuestaPc = "papel"
else:
	respuestaPc = "tijera"

print("PC eligió " + respuestaPc)
if respuestaPc == "piedra" and respuestaUsuario == "papel":
	resultado = "Ganaste!"
elif respuestaPc == "papel" and respuestaUsuario == "tijera":
	resultado = "Ganaste!"
elif respuestaPc == "tijera" and respuestaUsuario == "piedra":
	resultado = "Ganaste!"
elif respuestaPc == "papel" and respuestaUsuario == "piedra":
	resultado = "Perdiste!"
elif respuestaPc == "tijera" and respuestaUsuario == "papel":
	resultado = "Perdiste!"
elif respuestaPc == "piedra" and respuestaUsuario == "tijera":
	resultado = "Perdiste!"
elif respuestaPc == respuestaUsuario:
	resultado = "Empate"
else:
	resultado = "Así que ganó PC"
	print (resultado)

print("Gracias por jugar!")
