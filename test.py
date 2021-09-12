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

diagonalesDerecha = [
    [6, 1],
    [12, 7, 2],
    [18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [30, 25, 20, 15, 10, 5],
    [31, 26, 21, 16, 11],
    [32, 27, 22, 15],
    [33, 28, 23],
    [34, 29],
]

diagonalesIzquierda = [
    [24, 31],
    [18, 25, 32],
    [12, 19, 26, 33],
    [6, 13, 20, 27, 34],
    [0, 7, 14, 21, 28, 35],
    [1, 8, 15, 22, 29],
    [2, 9, 16, 23],
    [3, 10, 17],
    [4, 11],
]

tablero = [1,1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1]
jugadorActual = 1
pos = 35

def revisarDiagonalSuperiorIzq(tablero, jugadorActual, pos):
    for diagonal in diagonalesIzquierda:
        if pos in diagonal:
            arrDiagonal = diagonal
    cotaInferior = arrDiagonal[0]
    posicionDeFichasPorDarVuelta = []
    if(pos - 14 >= cotaInferior and tablero[pos - 7] == jugadorActual * -1): 
        indicePosEnColumnas = arrDiagonal.index(pos)
        arrayCasillasPorVerificar = arrDiagonal[0:indicePosEnColumnas]
        for posActual in arrayCasillasPorVerificar.__reversed__():
            fichaActual = tablero[posActual]
            if(fichaActual != jugadorActual):
                posicionDeFichasPorDarVuelta.append(posActual)
            if(fichaActual == jugadorActual):
                print('Fichas a dar vuelta: ', posicionDeFichasPorDarVuelta)
                return True
    return False
def revisarHaciaAbajo(tablero, jugadorActual, pos):
    numColumna = 0
    for fila in filas:
        if pos in fila:
            numColumna = fila.index(pos)
    cotaSuperior = columnas[numColumna][-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia abajo, y la ficha de la casilla de abajo debe ser del contrincante
    if(pos + 12 <= cotaSuperior and tablero[pos + 6] == jugadorActual * -1): 
        indicePosEnColumnas = columnas[numColumna].index(pos)
        arrayCasillasPorVerificar = columnas[numColumna][indicePosEnColumnas+1:]
        for posActual in arrayCasillasPorVerificar:
            fichaActual = tablero[posActual]
            if(fichaActual != jugadorActual):
                posicionDeFichasPorDarVuelta.append(posActual)
            if(fichaActual == jugadorActual):
                print('Fichas a dar vuelta: ', posicionDeFichasPorDarVuelta)
                return True
    return False
def revisarHaciaArriba(tablero, jugadorActual, pos):
    numColumna = 0
    for fila in filas:
        if pos in fila:
            numColumna = fila.index(pos)
    cotaInferior = columnas[numColumna][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia arriba, y la ficha de la casilla de arriba debe ser del contrincante
    if(pos - 12 >= cotaInferior and tablero[pos - 6] == jugadorActual * -1): 
        indicePosEnColumnas = columnas[numColumna].index(pos)
        arrayCasillasPorVerificar = columnas[numColumna][0:indicePosEnColumnas]
        for posActual in arrayCasillasPorVerificar.__reversed__():
            fichaActual = tablero[posActual]
            if(fichaActual != jugadorActual):
                posicionDeFichasPorDarVuelta.append(posActual)
            if(fichaActual == jugadorActual):
                print('Fichas a dar vuelta: ', posicionDeFichasPorDarVuelta)
                return True
    return False
def revisarHaciaIzquierda(tablero, jugadorActual, pos):
    numFila = 0
    for fila in filas:
        if pos in fila:
            numFila = filas.index(fila)
    cotaInferior = filas[numFila][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la izquierda, y la ficha de la casilla izquierda debe ser del contrincante
    if(pos - 2 >= cotaInferior and tablero[pos - 1] == jugadorActual * -1): 
        indicePosEnColumnas = filas[numFila].index(pos)
        arrayCasillasPorVerificar = filas[numFila][0:indicePosEnColumnas]
        print(arrayCasillasPorVerificar)
        for posActual in arrayCasillasPorVerificar.__reversed__():
            fichaActual = tablero[posActual]
            if(fichaActual != jugadorActual):
              posicionDeFichasPorDarVuelta.append(posActual)
            if(fichaActual == jugadorActual):
                print('Fichas a dar vuelta: ', posicionDeFichasPorDarVuelta)
                return True
    return False
def revisarHaciaDerecha(tablero, jugadorActual, pos):
    numFila = 0
    for fila in filas:
        if pos in fila:
            numFila = filas.index(fila)
    cotaSuperior = filas[numFila][-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la derecha, y la ficha de la casilla derecha debe ser del contrincante
    if(pos + 2 <= cotaSuperior and tablero[pos + 1] == jugadorActual * -1): 
        indicePosEnColumnas = filas[numFila].index(pos)
        arrayCasillasPorVerificar = filas[numFila][indicePosEnColumnas+1:]
        for posActual in arrayCasillasPorVerificar:
            fichaActual = tablero[posActual]
            if(fichaActual != jugadorActual):
              posicionDeFichasPorDarVuelta.append(posActual)
            if(fichaActual == jugadorActual):
                print('Fichas a dar vuelta: ', posicionDeFichasPorDarVuelta)
                return True
    return False

#print(revisarHaciaIzquierda(tablero, jugadorActual, pos))
#print(revisarHaciaDerecha(tablero, jugadorActual, pos))
#print(revisarHaciaArriba(tablero, jugadorActual, pos))
#print(revisarHaciaAbajo(tablero, jugadorActual, pos))
print(revisarDiagonalSuperiorIzq(tablero, jugadorActual, pos))





