import helpers
filas = helpers.filas
columnas = helpers.columnas
diagonalesDerecha = helpers.diagonalesDerecha
diagonalesIzquierda = helpers.diagonalesIzquierda
tamanio = 6*6
class JuegoReversi:
  #Comienza el raton, valor=1
  def __init__(self,turno=1):
    self.tablero=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.completo=False
    self.ganador=None
    self.jugador=turno
    self.fichasPorDarVuelta=[]
    self.agenteYusuarioSinJugadasPosibles=False

  def reiniciar(self):
    self.tablero=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.completo=False
    self.ganador=None
    self.jugador=1
    self.fichasPorDarVuelta = []
    self.agenteYusuarioSinJugadasPosibles=False

  def voltearFichas(self):
    for posFicha in self.fichasPorDarVuelta:
      self.tablero[posFicha] = self.tablero[posFicha] * -1
    self.fichasPorDarVuelta = []

  def revisarDiagonalSuperiorDer(self, pos):
    arrDiagonal = []
    cotaInferior = None
    for diagonal in diagonalesDerecha:
      if pos in diagonal:
        arrDiagonal = diagonal
        cotaInferior = arrDiagonal[0]
    posicionDeFichasPorDarVuelta = []
    if(cotaInferior != None and pos - 10 >= cotaInferior and self.tablero[pos - 5] == self.jugador * -1):
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalSuperiorIzq(self, pos):
    arrDiagonal = []
    cotaInferior = None
    for diagonal in diagonalesIzquierda:
      if pos in diagonal:
        arrDiagonal = diagonal
        cotaInferior = arrDiagonal[0]
    posicionDeFichasPorDarVuelta = []
    if(cotaInferior != None and pos - 14 >= cotaInferior and self.tablero[pos - 7] == self.jugador * -1): 
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaAbajo(self, pos):
    numColumna = 0
    cotaSuperior = None
    for fila in filas:
      if pos in fila:
        numColumna = fila.index(pos)
        cotaSuperior = columnas[numColumna][-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia abajo, y la ficha de la casilla de abajo debe ser del contrincante
    if(cotaSuperior != None and pos + 12 <= cotaSuperior and self.tablero[pos + 6] == self.jugador * -1): 
      indicePosEnColumnas = columnas[numColumna].index(pos)
      arrayCasillasPorVerificar = columnas[numColumna][indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaArriba(self, pos):
    numColumna = 0
    cotaInferior = None
    for fila in filas:
      if pos in fila:
        numColumna = fila.index(pos)
        cotaInferior = columnas[numColumna][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia arriba, y la ficha de la casilla de arriba debe ser del contrincante
    if(cotaInferior != None and pos - 12 >= cotaInferior and self.tablero[pos - 6] == self.jugador * -1): 
      indicePosEnColumnas = columnas[numColumna].index(pos)
      arrayCasillasPorVerificar = columnas[numColumna][0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaIzquierda(self, pos):
    numFila = 0
    cotaInferior = None
    for fila in filas:
      if pos in fila:
        numFila = filas.index(fila)
        cotaInferior = filas[numFila][0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la izquierda, y la ficha de la casilla izquierda debe ser del contrincante
    if(cotaInferior != None and pos - 2 >= cotaInferior and self.tablero[pos - 1] == self.jugador * -1): 
      indicePosEnColumnas = filas[numFila].index(pos)
      arrayCasillasPorVerificar = filas[numFila][0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaDerecha(self, pos):
    numFila = 0
    cotaSuperior = None
    for fila in filas:
      if pos in fila:
        numFila = filas.index(fila)
        cotaSuperior = filas[numFila][-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la derecha, y la ficha de la casilla derecha debe ser del contrincante
    if(cotaSuperior != None and pos + 2 <= cotaSuperior and self.tablero[pos + 1] == self.jugador * -1): 
      indicePosEnColumnas = filas[numFila].index(pos)
      arrayCasillasPorVerificar = filas[numFila][indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalInferiorIzq(self, pos):
    arrDiagonal = []
    cotaSuperior = None
    for diagonal in diagonalesDerecha:
      if pos in diagonal:
        arrDiagonal = diagonal
        cotaSuperior = arrDiagonal[-1]
    posicionDeFichasPorDarVuelta = []
    if(cotaSuperior != None and pos + 10 <= cotaSuperior and self.tablero[pos + 5] == self.jugador * -1):
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalInferiorDer(self, pos):
    arrDiagonal = []
    cotaSuperior = None
    for diagonal in diagonalesIzquierda:
      if pos in diagonal:
        arrDiagonal = diagonal
        cotaSuperior = arrDiagonal[-1]
    posicionDeFichasPorDarVuelta = []
    if(cotaSuperior != None and pos + 14 <= cotaSuperior and self.tablero[pos + 7] == self.jugador * -1): 
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador and fichaActual != 0):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  
  def generar_jugadas_posibles(self):
    posibles=[]
    for i in range(tamanio): 
      if self.tablero[i]==0:
        revisarHaciaIzquierda = self.revisarHaciaIzquierda(i)
        revisarHaciaDerecha = self.revisarHaciaDerecha(i)
        revisarHaciaArriba = self.revisarHaciaArriba(i)
        revisarHaciaAbajo = self.revisarHaciaAbajo(i)
        revisarDiagonalSuperiorDer = self.revisarDiagonalSuperiorDer(i)
        revisarDiagonalSuperiorIzq = self.revisarDiagonalSuperiorIzq(i)
        revisarDiagonalInferiorIzq = self.revisarDiagonalInferiorIzq(i)
        revisarDiagonalInferiorDer = self.revisarDiagonalInferiorDer(i)
        if(revisarHaciaIzquierda[0]):
          posibles.append([i, revisarHaciaIzquierda[1]])
        if(revisarHaciaDerecha[0]):
          posibles.append([i, revisarHaciaDerecha[1]])
        if(revisarHaciaArriba[0]):
          posibles.append([i, revisarHaciaArriba[1]])
        if(revisarHaciaAbajo[0]):
          posibles.append([i, revisarHaciaAbajo[1]])
        if(revisarDiagonalSuperiorDer[0]):
          posibles.append([i, revisarDiagonalSuperiorDer[1]])
        if(revisarDiagonalSuperiorIzq[0]):
          posibles.append([i, revisarDiagonalSuperiorIzq[1]])
        if(revisarDiagonalInferiorIzq[0]):
          posibles.append([i, revisarDiagonalInferiorIzq[1]])
        if(revisarDiagonalInferiorDer[0]):
          posibles.append([i, revisarDiagonalInferiorDer[1]])
    return posibles

  def estado_final(self):
    self.evaluar(False)
    if self.completo or self.agenteYusuarioSinJugadasPosibles:
      return True
    else:
      return False

  def evaluar(self, depthTerminado):
    if 0 not in self.tablero:
      self.completo=True
    else:
      self.completo=False
    if self.completo or self.agenteYusuarioSinJugadasPosibles or depthTerminado:
      if(self.tablero.count(1) > self.tablero.count(-1)):
        self.ganador=1
      elif(self.tablero.count(1) == self.tablero.count(-1)):
        self.ganador=0
      else:
        self.ganador=-1

  def calcular_utilidad(self):
    return self.ganador

  def jugar(self,jugada):
    self.tablero[jugada]=self.jugador
    self.jugador*=-1

  def deshacer_jugada(self,jugada):
    self.tablero[jugada]=0
    self.jugador*=-1

#IA
def minimax(depth, juego,etapa,secuencia,secuencias):
  depth -= 1
  if juego.estado_final() or depth == 0:
    if(depth == 0):
      juego.evaluar(True)
    secuencias.append(secuencia.copy())
    return [-1*juego.calcular_utilidad()]
  if etapa==1:
    valor=[-1000,None]
  else:
    valor=[1000,None]
  jugadas_posibles=juego.generar_jugadas_posibles()
  for jugada in jugadas_posibles:
    juego.jugar(jugada[0])
    secuencia.append(jugada[0])
    opcion=minimax(depth, juego, etapa*-1, secuencia, secuencias)
    #maximizar
    if etapa==1:
      if valor[0]<opcion[0]:
        valor=[opcion[0],jugada[0],jugada[1]]
    else:
    #minimizar
      if valor[0]>opcion[0]:
        valor=[opcion[0],jugada[0],jugada[1]]
    juego.deshacer_jugada(jugada[0])
    secuencia.pop()
  return valor