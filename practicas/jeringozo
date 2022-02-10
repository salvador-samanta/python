#transforma en jeringozo cualquier texto que introduzca el usuario:

def jeringozo(frase):
    j = ''
    anterior = ''
    
    for letra in frase:
        if anterior in 'q' and letra in 'u':
            j = j + letra
        elif letra in 'aeiouyáéíóú':
            j = j + letra + 'p' + letra
        elif anterior in 'aeiouáéíóú' and letra in 'aeiouáéíóú':
            j = j + letra
        else:
            j = j + letra
        anterior = letra
    print(j)


el_texto = input("Ingresá frase: ")
jeringozo(el_texto)
