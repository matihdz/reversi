import test

filas = test.filas
columnas = test.columnas
diagonalesDerecha = test.diagonalesDerecha
diagonalesIzquierda = test.diagonalesIzquierda
tamanio = 6*6
class JuegoGato:
  #Comienza el raton, valor=1
  def __init__(self,turno=1):
    self.tablero=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.completo=False
    self.ganador=None
    self.jugador=turno
    self.fichasPorDarVuelta=[]

  def reiniciar(self):
    self.tablero=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.completo=False
    self.ganador=None
    self.jugador=1
    self.fichasPorDarVuelta = []

  def voltearFichas(self):
    for posFicha in self.fichasPorDarVuelta:
      print(self.fichasPorDarVuelta, 'uwu')
      self.tablero[posFicha] = self.tablero[posFicha] * -1
    self.fichasPorDarVuelta = []

  def voltearFichas2(self):
    for posFicha in self.fichasPorDarVuelta:
      print(posFicha)
      self.tablero[posFicha] = self.tablero[posFicha] * -1
    self.fichasPorDarVuelta = []

  def definicion_diagonal(self, ficha):
    for diagonal in diagonalesDerecha:
      if ficha in diagonal:
        return diagonal

  def func_busqueda_recursiva_posibles(self, diagonal, ficha, dist_diagonal):
    lista_fichas_por_voltear = []
    if ficha + dist_diagonal not in diagonal:
      return lista_fichas_por_voltear
    elif self.tablero[ficha + dist_diagonal] == (self.jugador * -1):
      lista_fichas_por_voltear.append(self.tablero[ficha + dist_diagonal])
      self.func_busqueda_recursiva_posibles(self, diagonal, ficha, dist_diagonal-5)
    

    '''if self.tablero[pos] == 0:
      if self.tablero[diagonal[1]] == self.jugador*-1:
        self.tablero[diagonal[1]] = self.jugador
    else:
      print('no se puede uwu')'''
  
  def asignar_lineas(self, pos):
    
    f = pos/6
    c = pos%6
    fila = filas[f]
    columna = columnas[c]
    filaIndex = fila.index(pos)
    columnaIndex = columna.index(pos)
    arrDiagonalD = []
    arrDiagonalI = []

    if filaIndex == columnaIndex:
      arrDiagonalI = diagonalesIzquierda[3]
      if filaIndex > 0 and filaIndex < 5:
        arrDiagonalD = diagonalesDerecha[filaIndex-1]
    elif pos != 0 and pos%5 == 0:
      arrDiagonalD = diagonalesDerecha[3]
      if filaIndex > 0 and filaIndex < 5:
        arrDiagonalI = diagonalesIzquierda[filaIndex-1]

    if filaIndex > 0 and pos not in [13,19,25,20,25,26,27]:
      if filaIndex == columnaIndex - 1:
        arrDiagonalI = diagonalesIzquierda[4]
      elif filaIndex == columnaIndex - 2:
        arrDiagonalI = diagonalesIzquierda[5]
      elif filaIndex == columnaIndex - 3:
        arrDiagonalI = diagonalesIzquierda[6]

      elif filaIndex - 1 == columnaIndex:
        arrDiagonalD = diagonalesDerecha[2]
      elif filaIndex - 2 == columnaIndex:
        arrDiagonalD = diagonalesDerecha[1]


    

    elif pos > 1 and pos < 4:
      if pos == 2:
        arrDiagonalD = diagonalesDerecha[0]
        arrDiagonalI = diagonalesIzquierda[5]
      if pos == 3:
        arrDiagonalD = diagonalesDerecha[1]
        arrDiagonalI = diagonalesIzquierda[6]



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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
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
          self.fichasPorDarVuelta = posicionDeFichasPorDarVuelta
        if(fichaActual == self.jugador):
          return True
    return False
  
  def generar_jugadas_posibles(self): #Acá se ve que, porque y como jugara el agente
    posibles=[]
    for i in range(tamanio): 
      if self.tablero[i]==0:
        '''self.func_busqueda_recursiva_posibles(self.definicion_diagonal(i), i, -5)'''
        if(self.revisarHaciaIzquierda(i)):
          posibles.append(i)
        if(self.revisarHaciaDerecha(i)):
          posibles.append(i)
        if(self.revisarHaciaArriba(i)):
          posibles.append(i)
        if(self.revisarHaciaAbajo(i)):
          posibles.append(i)
        if(self.revisarDiagonalSuperiorDer(i)):
          posibles.append(i)
        if(self.revisarDiagonalSuperiorIzq(i)):
          posibles.append(i)
        if(self.revisarDiagonalInferiorIzq(i)):
          posibles.append(i)
        if(self.revisarDiagonalInferiorDer(i)):
          posibles.append(i)
    print(posibles)
    return posibles

  def estado_final(self):
    self.evaluar()
    if self.completo:
      return True
    else:
      return False

  def evaluar(self):
    if 0 not in self.tablero:
      self.completo=True
    else:
      self.completo=False
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
def alfabeta2(depth, juego, etapa, alfa, beta, secuencia, secuencias):
  print(juego.tablero)
  jugadas_posibles = juego.generar_jugadas_posibles()
  juego.voltearFichas()
  if len(jugadas_posibles) != 0:
    return [juego.jugador, jugadas_posibles[0]]
  else:
    return []

  # correctamente el metodo "generar_jugadas_posibles"
  #1 objetivo: Que funcione el agente al azar
  #2 objetivo: Que funcione el agente con sistema de puntos/ depth / etc








def alfabeta(depth, juego, etapa, alfa, beta, secuencia, secuencias):
  if depth == 0 or juego.estado_final():
    secuencias.append(secuencia.copy())
    return [-1*juego.calcular_utilidad()]
  if etapa==1:
    valor=[-1000,None]
  else:
    valor=[1000,None]
  jugadas_posibles=juego.generar_jugadas_posibles()
  for jugada in jugadas_posibles:
    juego.jugar(jugada)
    secuencia.append(jugada)
    opcion=alfabeta(depth -1 ,juego, etapa*-1, alfa, beta, secuencia, secuencias)
    if etapa==1:
      if valor[0]<opcion[0]:
        valor=[opcion[0],jugada]
      if valor[0]>alfa:
        alfa=valor[0]
      if valor[0]>=beta:
        juego.deshacer_jugada(jugada)
        secuencia.pop()
        break
    else:
      if valor[0]>opcion[0]:
        valor=[opcion[0],jugada]
      if valor[0]<beta:
        beta=valor[0]
      if valor[0]<=alfa:
        juego.deshacer_jugada(jugada)
        secuencia.pop()
        break
    juego.deshacer_jugada(jugada)
    secuencia.pop()
  juego.voltearFichas()
  return valor

if __name__ == "__main__":
  juego=JuegoGato(-1)
  o3=[]
  r3=alfabeta(5,juego,-1,-1000,1000,[],o3)