import aisearch
import time
from tkinter import *
from tkinter import messagebox


class ventanaDificultad:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Dificultad")
        self.ventana.configure(bg = "grey")
        self.dificultad = 4
        etiqueta = Label(text = "Seleccione la dificultad. \n(Dificultad baja seleccionada por defecto)", bg = "grey")
        boton1 = Button(self.ventana, bg = "lightblue", text = 'Baja', width = 16, height = 3, command = lambda: self.setDificultad(4))
        boton2 = Button(self.ventana, bg = "orange", text = 'Media', width = 16, height = 3, command = lambda: self.setDificultad(5))
        boton3 = Button(self.ventana, bg = "red", text = 'Alta', width = 16, height = 3, command = lambda: self.setDificultad(6))
        boton4 = Button(self.ventana, bg = "lightgreen", text = '¡A jugar!', width = 16, height = 3, command = lambda: self.setDificultad(4))
        etiqueta.pack()
        boton1.pack()
        boton2.pack()
        boton3.pack()
        boton4.pack()

    def setDificultad(self, i):
        self.dificultad = i
        self.ventana.destroy
        Reversi(i)

class Reversi:
    def __init__(self, dificultad):
        self.principal = Toplevel()
        self.principal.title("Reversi")
        self.botones=[]
        self.dificultadPorProfundidad = dificultad
        self.agente=PhotoImage(file="./resources/agente.png")
        self.usuario=PhotoImage(file="./resources/usuario.png")
        self.vacio=PhotoImage(file="./resources/vacio.png")
        self.juego=aisearch.JuegoReversi()
        self.actualizar_tablero()
        print (self.dificultadPorProfundidad)

    def actualizar_tablero(self):
        k = 0
        for i in range(6):
            fila=[]
            for j in range(6):
                if (self.juego.tablero[k] == 0):
                    b1=Button(self.principal, image=self.vacio,width="80",height="80")
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
        if self.juego.estado_final():
            if self.juego.ganador == 1:
                messagebox.showinfo("Reversi", "Has ganado!")
                self.principal.after(2500,lambda:self.principal.destroy())
            elif self.juego.ganador == 0:
                messagebox.showinfo("Reversi", "Empate")
                self.principal.after(2500,lambda:self.principal.destroy())
            else:
                messagebox.showinfo("Reversi", "Has perdido")
                self.principal.after(2500,lambda:self.principal.destroy())
            return True
        else:
            return False

    def agenteJuegaDeNuevo(self):
        jugadas_posibles = self.juego.generar_jugadas_posibles()
        if len(jugadas_posibles) != 0:
            #m = aisearch.alfabetaAzar(self.juego)
            m = aisearch.minimax(self.dificultadPorProfundidad,self.juego, -1000, 1000,  1, [], [])
            self.juego.jugar(m[1])
            self.juego.fichasPorDarVuelta = m[2]
            self.juego.voltearFichas()
            self.actualizar_tablero()
            self.victoria()
        elif len(jugadas_posibles) == 0:
            print('El agente y el usuario no tienen jugadas posibles, se termina el encuentro')
            self.juego.agenteYusuarioSinJugadasPosibles = True
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
                            jugadas_posibles = self.juego.generar_jugadas_posibles()
                            if len(jugadas_posibles) != 0:
                                #m = aisearch.alfabetaAzar(self.juego)
                                m=aisearch.minimax(self.dificultadPorProfundidad,self.juego, -1000, 1000,  1, [], [])
                                if(m[1] != None):
                                    self.juego.jugar(m[1])
                                    self.juego.fichasPorDarVuelta = m[2]
                                    self.juego.voltearFichas()
                                    self.actualizar_tablero()
                                    self.victoria()
                                else:
                                    print('El agente no tiene jugadas posibles, turno del usuario')
                                    self.juego.jugador*=-1
                                    return
                            elif len(jugadas_posibles) == 0:
                                print('El agente no tiene jugadas posibles, turno del usuario')
                                self.juego.jugador*=-1
                                return
            else:
                print('Tienes que jugar la ficha en una casilla vacia')
        elif len(jugadas_posibles) == 0:
            print('El usuario no tiene jugadas posibles, turno del agente')
            time.sleep(1)
            self.juego.jugador*=-1
            self.agenteJuegaDeNuevo()

juego = ventanaDificultad()
mainloop()
