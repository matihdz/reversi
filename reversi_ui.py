import aisearch
from tkinter import *
from tkinter import messagebox
class Reversi:
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Reversi")
        self.botones=[]
        self.agente=PhotoImage(file="./resources/agente.png")
        self.usuario=PhotoImage(file="./resources/usuario.png")
        self.vacio=PhotoImage(file="./resources/vacio.png")
        self.juego=aisearch.JuegoReversi()
        self.agenteYusuarioSinJugadasPosibles = False
        self.actualizar_tablero()

    def actualizar_tablero(self):
        k = 0
        for i in range(6):
            fila=[]
            for j in range(6):
                if (self.juego.tablero[k] == 0):
                    b1=Button(self.principal,image=self.vacio,width="80",height="80")
                elif (self.juego.tablero[k] == 1):
                    b1 = Button(self.principal, image=self.usuario, width="80", height="80")
                elif (self.juego.tablero[k] == -1):
                    b1 = Button(self.principal, image=self.agente, width="80", height="80")
                b1.bind("<Button-1>",self.click)
                b1.x=i
                b1.y=j
                b1.grid(row=i,column=j)
                fila.append(b1)
                k += 1
            self.botones.append(fila)


    def victoria(self):
        #fix: cuando entra al if por "self.agenteYusuarioSinJugadasPosibles", no determina ganador, ya que no
        #pasa por "self.juego.estado_final()"
        #fix2: solo cuando el tablero está completo se termina el juego? es realmente la unica condicion de parada?
        #(evaluar 'fix2'!!)
        if self.juego.estado_final() or self.agenteYusuarioSinJugadasPosibles:
            if self.juego.ganador == 1:
                messagebox.showinfo("Reversi", "Has ganado!")
            elif self.juego.ganador == 0:
                messagebox.showinfo("Reversi", "Empate")
            else:
                messagebox.showinfo("Reversi", "Has perdido")
            self.agenteYusuarioSinJugadasPosibles = False
            self.juego.reiniciar()
            self.actualizar_tablero()           
            return True
        else:
            return False

    def agenteJuegaDeNuevo(self):
        m = aisearch.alfabeta2(10, self.juego, 1,-1000, 1000, [], [])
        if(m):
            self.juego.jugar(m[1])
            self.juego.voltearFichas()
            self.actualizar_tablero()
            self.victoria()
        else:
            print('El agente y el usuario no tienen jugadas posibles, se termina el encuentro')
            self.agenteYusuarioSinJugadasPosibles = True
            self.victoria()

    def click(self,evento):
        jugadas_posibles = self.juego.generar_jugadas_posibles()
        if len(jugadas_posibles) != 0:
            ficha_jugador = evento.widget.x * 6 + evento.widget.y
            if self.juego.tablero[ficha_jugador]==0:
                for jugada in jugadas_posibles:
                    if ficha_jugador == jugada[0]:
                        self.juego.jugar(ficha_jugador)
                        self.juego.fichasPorDarVuelta = jugada[1]
                        self.juego.voltearFichas()
                        self.actualizar_tablero()
                        if not self.victoria():
                            m = aisearch.alfabeta2(10, self.juego, 1,-1000, 1000, [], [])
                            if(m):
                                self.juego.jugar(m[1])
                                self.juego.voltearFichas()
                                self.actualizar_tablero()
                                self.victoria()
                            else:
                                print('El agente no tiene jugadas posibles, turno del usuario')
                                self.juego.jugador*=-1
                                return
            else:
                print('Tienes que jugar la ficha en una casilla vacia')
        elif len(jugadas_posibles) == 0:
            print('El usuario no tiene jugadas posibles, turno del agente')
            self.juego.jugador*=-1
            self.agenteJuegaDeNuevo()


juego=Reversi()
mainloop()
