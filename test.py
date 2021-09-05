filas = [
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29],
    [30, 31, 32, 33, 34, 35],
]
columnas = [
    [0, 6, 12, 18, 24, 30], 
    [1, 7, 13, 19, 25, 31], 
    [2, 8, 14, 20, 26, 32], 
    [3, 9, 15, 21, 27, 33], 
    [4, 10, 16, 22, 28, 34], 
    [5, 11, 17, 23, 29, 35], 
]

tablero = [1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
jugadorActual = 1
pos = 19

# en "revisarHaciaArriba" faltan cosas
def revisarHaciaArriba(tablero, jugadorActual, pos):
    numFila = 0
    numColumna = 0
    for fila in filas:
        if pos in fila:
            numFila = filas.index(fila)
            numColumna = fila.index(pos)

    cotaInferior = columnas[numColumna][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia arriba, y la ficha de la casilla de arriba debe ser del contrincante
    if(pos - 12 >= cotaInferior and tablero[pos - 6] == jugadorActual * -1): 
        cantidadCasillasPorVerificar = 0
        for casilla in columnas[numColumna]:
            if(casilla == pos):
                break
            cantidadCasillasPorVerificar = cantidadCasillasPorVerificar + 1
        seisEnSeis = 0
        while cantidadCasillasPorVerificar >= 0:
            fichaActual = tablero[cotaInferior + seisEnSeis]
            print(cotaInferior)
            if(fichaActual == jugadorActual):
                return 'termino la revision hacia arriba, esta es una posible jugada'
            if(cantidadCasillasPorVerificar == 0):
                return 'termino la revision hacia arriba, esta NO es una posible jugada'
            posicionDeFichasPorDarVuelta.append(cotaInferior + seisEnSeis)
            print(posicionDeFichasPorDarVuelta)
            seisEnSeis = seisEnSeis + 6
            cantidadCasillasPorVerificar = cantidadCasillasPorVerificar - 1
def revisarHaciaIzquierda(tablero, jugadorActual, pos):
    numFila = 0
    numColumna = 0
    for fila in filas:
        if pos in fila:
            numFila = filas.index(fila)
            numColumna = fila.index(pos)

    cotaInferior = filas[numFila][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la izquierda, y la ficha de la casilla izquierda debe ser del contrincante
    if(pos - 2 >= cotaInferior and tablero[pos - 1] == jugadorActual * -1): 
        cantidadCasillasPorVerificar = pos - cotaInferior - 1
        while cantidadCasillasPorVerificar >= 0:
            fichaActual = tablero[cotaInferior + cantidadCasillasPorVerificar]
            if(fichaActual == jugadorActual):
                return 'termino la revision hacia la izquierda, esta es una posible jugada'
            posicionDeFichasPorDarVuelta.append(cotaInferior + cantidadCasillasPorVerificar)
            print(posicionDeFichasPorDarVuelta)
            cantidadCasillasPorVerificar = cantidadCasillasPorVerificar - 1
def revisarHaciaDerecha(tablero, jugadorActual, pos):
    numFila = 0
    numColumna = 0
    for fila in filas:
        if pos in fila:
            numFila = filas.index(fila)
            numColumna = fila.index(pos)

    cotaInferior = filas[numFila][0]
    cotaSuperior = filas[numFila][-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la derecha, y la ficha de la casilla derecha debe ser del contrincante
    if(pos + 2 <= cotaSuperior and tablero[pos + 1] == jugadorActual * -1): 
        if(pos == 0):
            cantidadCasillasPorVerificar = cotaSuperior - 1
        else:
            cantidadCasillasPorVerificar = cotaSuperior - pos + 1
        print(cantidadCasillasPorVerificar)
        while cantidadCasillasPorVerificar >= 0:
            fichaActual = tablero[cotaSuperior - cantidadCasillasPorVerificar]
            if(fichaActual == jugadorActual):
                return 'termino la revision hacia la derecha, esta es una posible jugada'
            if(cantidadCasillasPorVerificar == 0):
                return 'termino la revision hacia la derecha, esta NO es una posible jugada'
            posicionDeFichasPorDarVuelta.append(cotaSuperior - cantidadCasillasPorVerificar)
            print(posicionDeFichasPorDarVuelta)
            cantidadCasillasPorVerificar = cantidadCasillasPorVerificar - 1

#Hay unas condiciones que me faltaron en las funciones ya hechas, y faltan implementar todas las revisiones menos
#las horizontales (izq y der)

#print(revisarHaciaIzquierda(tablero, jugadorActual, pos))
#print(revisarHaciaDerecha(tablero, jugadorActual, pos))
print(revisarHaciaArriba(tablero, jugadorActual, pos))





