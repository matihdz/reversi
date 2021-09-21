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
    self.listaArreglos = self.asignar_lineas()
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

  def asignar_lineas(self):
    conjuntoDeListas = []
    for pos in range(36):
      f = int(pos/6)
      c = pos%6
      fila = filas[f]
      columna = columnas[c]
      arrDiagonalD = []
      arrDiagonalI = []
      listaConLineas = []

      restoEntre7 = pos % 7
      restoEntre10 = pos % 10

      if pos not in [4, 5, 11, 24, 30, 31]:
        if fila.index(pos) == columna.index(pos):
          arrDiagonalI = diagonalesIzquierda[3]
        elif restoEntre7 == 4:
          arrDiagonalI = diagonalesIzquierda[0]
        elif restoEntre7 == 5:
          arrDiagonalI = diagonalesIzquierda[1]
        elif restoEntre7 == 6:
          arrDiagonalI = diagonalesIzquierda[2]
        elif restoEntre7 == 1:
          arrDiagonalI = diagonalesIzquierda[4]
        elif restoEntre7 == 2:
          arrDiagonalI = diagonalesIzquierda[5]
        elif restoEntre7 == 3:
          arrDiagonalI = diagonalesIzquierda[6]
      
      
      if pos not in [0, 1, 6, 29, 34, 35]:
        if pos % 5 == 0 and pos != 35:
          arrDiagonalD = diagonalesDerecha[3]
        else:
          if restoEntre10 == 2 or restoEntre10 == 7:
            if (pos < 22 or pos == 24) and pos != 17:
              arrDiagonalD = diagonalesDerecha[0]
            elif (pos > 21 and pos != 24) or pos == 17:
              arrDiagonalD = diagonalesDerecha[5]
          elif restoEntre10 == 3 or restoEntre10 == 8:  
            if pos < 22:
              arrDiagonalD = diagonalesDerecha[1]
            elif pos > 21:
              arrDiagonalD = diagonalesDerecha[6]
          if restoEntre10 == 4 or restoEntre10 == 9:
            arrDiagonalD = diagonalesDerecha[2]
          elif restoEntre10 == 1 or restoEntre10 == 6:
            arrDiagonalD = diagonalesDerecha[4]
      
      
      listaConLineas.append(fila)
      listaConLineas.append(columna)
      listaConLineas.append(arrDiagonalD)
      listaConLineas.append(arrDiagonalI)
      conjuntoDeListas.append(listaConLineas)
    return conjuntoDeListas

  def revisarDiagonalSuperiorDer(self, arrDiagonal, pos):
    cotaInferior = arrDiagonal[0]
    posicionDeFichasPorDarVuelta = []
    if(pos - 10 >= cotaInferior and self.tablero[pos - 5] == self.jugador * -1):
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalSuperiorIzq(self, arrDiagonal, pos):
    cotaInferior = arrDiagonal[0]
    posicionDeFichasPorDarVuelta = []
    if(pos - 14 >= cotaInferior and self.tablero[pos - 7] == self.jugador * -1): 
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaAbajo(self, columna, pos):
    cotaSuperior = None
    cotaSuperior = columna[-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia abajo, y la ficha de la casilla de abajo debe ser del contrincante
    if(pos + 12 <= cotaSuperior and self.tablero[pos + 6] == self.jugador * -1): 
      indicePosEnColumnas = columna.index(pos)
      arrayCasillasPorVerificar = columna[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaArriba(self, columna, pos):
    cotaInferior = columna[0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia arriba, y la ficha de la casilla de arriba debe ser del contrincante
    if(pos - 12 >= cotaInferior and self.tablero[pos - 6] == self.jugador * -1): 
      indicePosEnColumnas = columna.index(pos)
      arrayCasillasPorVerificar = columna[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaIzquierda(self, fila, pos):
    numFila = 0
    cotaInferior = fila[0]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la izquierda, y la ficha de la casilla izquierda debe ser del contrincante
    if(pos - 2 >= cotaInferior and self.tablero[pos - 1] == self.jugador * -1): 
      indicePosEnColumnas = fila.index(pos)
      arrayCasillasPorVerificar = fila[0:indicePosEnColumnas]
      for posActual in arrayCasillasPorVerificar.__reversed__():
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarHaciaDerecha(self, fila, pos):
    cotaSuperior = fila[-1]
    posicionDeFichasPorDarVuelta = []
    #Deben haber al menos 2 espacios hacia la derecha, y la ficha de la casilla derecha debe ser del contrincante
    if(pos + 2 <= cotaSuperior and self.tablero[pos + 1] == self.jugador * -1): 
      indicePosEnColumnas = fila.index(pos)
      arrayCasillasPorVerificar = fila[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalInferiorIzq(self, arrDiagonal, pos):
    cotaSuperior = arrDiagonal[-1]
    posicionDeFichasPorDarVuelta = []
    if(pos + 10 <= cotaSuperior and self.tablero[pos + 5] == self.jugador * -1):
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]
  def revisarDiagonalInferiorDer(self, arrDiagonal, pos):
    cotaSuperior = arrDiagonal[-1]
    posicionDeFichasPorDarVuelta = []
    if(pos + 14 <= cotaSuperior and self.tablero[pos + 7] == self.jugador * -1): 
      indicePosEnColumnas = arrDiagonal.index(pos)
      arrayCasillasPorVerificar = arrDiagonal[indicePosEnColumnas+1:]
      for posActual in arrayCasillasPorVerificar:
        fichaActual = self.tablero[posActual]
        if(fichaActual != self.jugador):
          posicionDeFichasPorDarVuelta.append(posActual)
        if(fichaActual == self.jugador):
          return [True, posicionDeFichasPorDarVuelta]
    return [False, []]


  def generar_jugadas_posibles(self): #Acá se ve que, porque y como jugara el agente
    posibles=[]
    for i in range(36): 
      if self.tablero[i]==0:
        revisarHaciaIzquierda = self.revisarHaciaIzquierda(self.listaArreglos[i][0], i)
        revisarHaciaDerecha = self.revisarHaciaDerecha(self.listaArreglos[i][0], i)
        revisarHaciaArriba = self.revisarHaciaArriba(self.listaArreglos[i][1], i)
        revisarHaciaAbajo = self.revisarHaciaAbajo(self.listaArreglos[i][1], i)
        revisarDiagonalSuperiorDer = []
        revisarDiagonalInferiorDer = []
        revisarDiagonalSuperiorIzq = []
        revisarDiagonalInferiorIzq = []
        if self.listaArreglos[i][2]:
          revisarDiagonalSuperiorDer = self.revisarDiagonalSuperiorDer(self.listaArreglos[i][2], i)
          revisarDiagonalInferiorIzq = self.revisarDiagonalInferiorIzq(self.listaArreglos[i][2], i)
        if self.listaArreglos[i][3]:
          revisarDiagonalSuperiorIzq = self.revisarDiagonalSuperiorIzq(self.listaArreglos[i][3], i)
          revisarDiagonalInferiorDer = self.revisarDiagonalInferiorDer(self.listaArreglos[i][3], i)
          
        if(revisarHaciaIzquierda and revisarHaciaIzquierda[0]):
          posibles.append([i, revisarHaciaIzquierda[1]])
        if(revisarHaciaDerecha and revisarHaciaDerecha[0]):
          posibles.append([i, revisarHaciaDerecha[1]])
        if(revisarHaciaArriba and revisarHaciaArriba[0]):
          posibles.append([i, revisarHaciaArriba[1]])
        if(revisarHaciaAbajo and revisarHaciaAbajo[0]):
          posibles.append([i, revisarHaciaAbajo[1]])
        if(revisarDiagonalSuperiorDer and revisarDiagonalSuperiorDer[0]):
          posibles.append([i, revisarDiagonalSuperiorDer[1]])
        if(revisarDiagonalSuperiorIzq and revisarDiagonalSuperiorIzq[0]):
          posibles.append([i, revisarDiagonalSuperiorIzq[1]])
        if(revisarDiagonalInferiorIzq and revisarDiagonalInferiorIzq[0]):
          posibles.append([i, revisarDiagonalInferiorIzq[1]])
        if(revisarDiagonalInferiorDer and revisarDiagonalInferiorDer[0]):
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

lista_ponderaciones= [20, -4, 0.7, 0.7, -4, 20,  -5, -2, -0.1, -0.1, -2, -5,  1.5, -0.5, 0.5, 0.5, -0.5, 1.5,  1.5, -0.5, 0.5, 0.5, -0.5, 1.5,  -5, -2, -0.1, -0.1, -2, -5,  20, -4, 0.7, 0.7, -4, 20]

def alfabeta(depth, juego, alpha, beta, etapa,secuencia,secuencias):
  depth -= 1
  if juego.estado_final() or depth == 0:
    if(depth == 0):
      juego.evaluar(True)
    secuencias.append(secuencia.copy())
    return [-1*juego.calcular_utilidad()]
  if etapa==1:
    valor=[alpha,None]
  else:
    valor=[beta,None]
  jugadas_posibles=juego.generar_jugadas_posibles()
  for jugada in jugadas_posibles:
    juego.jugar(jugada[0])
    secuencia.append(jugada[0])
    opcion=alfabeta(depth, juego, alpha, beta, etapa*-1, secuencia, secuencias)
    puntaje_fichas_volteadas = 0
    for i in jugada[1]:
      puntaje_fichas_volteadas = lista_ponderaciones[i] + puntaje_fichas_volteadas
    opcion[0] = lista_ponderaciones[jugada[0]] + puntaje_fichas_volteadas
    juego.deshacer_jugada(jugada[0])
    #maximizar
    if etapa==1:
      if valor[0]<opcion[0]:
        valor=[opcion[0],jugada[0],jugada[1]]
        alpha = valor[0]
      else:
        break
    else:
    #minimizar
      if valor[0]>opcion[0]:
        valor=[opcion[0],jugada[0],jugada[1]]
        beta = valor[0]
      else:
        break
    secuencia.pop()
  return valor


