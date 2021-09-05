""" 
if(i-6 >= 0 and i-12 >= 0):
  if(self.tablero[i-6] == self.jugador*-1 and self.tablero[i-12] == self.jugador): #Verificar hacia arriba
    posibles.append(i)
if(i+6 <= 36 and i+12 <= 36):
  print(i)
  if(self.tablero[i+6] == self.jugador*-1 and self.tablero[i+12] == self.jugador): #Verificar hacia abajo
    posibles.append(i)
if(i-1 >= 0 and i-2 >= 0):
  if(self.tablero[i-1] == self.jugador*-1 and self.tablero[i-2] == self.jugador): #Verificar hacia izq
    posibles.append(i)
if(i+1 <= 36 and i+2 <= 36):
  if(self.tablero[i+1] == self.jugador*-1 and self.tablero[i+2] == self.jugador): #Verificar hacia der
    posibles.append(i)
if(i-7 >= 0 and i-14 >= 0):
  if(self.tablero[i-7] == self.jugador*-1 and self.tablero[i-14] == self.jugador): #Verificar hacia diag. sup. izq.
    posibles.append(i)
if(i-5 >= 0 and i-10 >= 0):
  if(self.tablero[i-5] == self.jugador*-1 and self.tablero[i-10] == self.jugador): #Verificar hacia diag. sup. der.
    posibles.append(i)
if(i+5 <= 36 and i+10 <= 36):
  if(self.tablero[i+5] == self.jugador*-1 and self.tablero[i+10] == self.jugador): #Verificar hacia diag. inf. izq.
    posibles.append(i)
if(i+7 <= 36 and i+14 <= 36):
  if(self.tablero[i+7] == self.jugador*-1 and self.tablero[i+14] == self.jugador): #Verificar hacia diag. inf. der.
    posibles.append(i)
"""
def evaluar(self): #¿Gano alguien? ¿Quién ganó?
    if 0 not in self.tablero:
      self.completo=True
    else:
      self.completo=False
    estado=[]
    for i in [0,3,6]:
      estado.append(sum(self.tablero[i:i+3]))
    for i in [0,1,2]:
      estado.append(self.tablero[i]+self.tablero[i+3]+self.tablero[i+6])
    estado.append(self.tablero[0]+self.tablero[4]+self.tablero[8])
    estado.append(self.tablero[2]+self.tablero[4]+self.tablero[6])
    for valor in estado:
      if valor==3 or valor==-3:
        self.ganador=valor//3
        return
    if self.completo:
      self.ganador=0
    else:
      self.ganador=None
def alfabeta(juego,etapa,alfa,beta,secuencia,secuencias):
  if juego.estado_final():
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
    opcion=alfabeta(juego,etapa*-1,alfa,beta,secuencia,secuencias)
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
  return valor