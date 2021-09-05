tamanio = 3 * 3

class JuegoGato:
  #Comienza el raton, valor=1
  def __init__(self,estado=[0]*tamanio,turno=1):
    self.tablero=estado
    self.completo=False
    self.ganador=None
    self.jugador=turno

  def reiniciar(self):
    self.tablero=[0]*tamanio
    self.completo=False
    self.ganador=None
    self.jugador=1

  def generar_jugadas_posibles(self): #Acá se ve que, porque y como jugara el agente
    posibles=[]
    print(self.tablero)
    for i in range(tamanio):
      if self.tablero[i]==0:
        posibles.append(i)
    return posibles

  def estado_final(self):
    self.evaluar()
    if self.ganador is not None or self.completo:
      return True
    else:
      return False

  def evaluar(self): #Acá se ve que, porque y como jugara el agente
    if 0 not in self.tablero:
      self.completo=True
    else:
      self.completo=False
    if self.completo:
      if(self.tablero.count(1) > self.tablero.count(-1)):
        self.ganador=1
      elif(self.tablero.count(1) == self.tablero.count(-1)):
        self.ganador=0
      else:
        self.ganador=-1
    else:
      self.ganador=None

  def calcular_utilidad(self):
    return self.ganador

  def jugar(self,jugada):
    self.tablero[jugada]=self.jugador
    self.jugador*=-1

  def deshacer_jugada(self,jugada):
    self.tablero[jugada]=0
    self.jugador*=-1

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


if __name__ == "__main__":
  juego=JuegoGato([0,0,0,0,0,0,0,0,0],-1)
  o3=[]
  r3=alfabeta(juego,-1,-1000,1000,[],o3)
