import aisearch
from tkinter import *
from tkinter import messagebox

tamanio = 6
class Gato:
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Reversi")
        self.botones=[]
        self.gato=PhotoImage(file="./resources/agente.png")
        self.raton=PhotoImage(file="./resources/usuario.png")
        self.vacio=PhotoImage(file="./resources/vacio.png")
        self.juego=aisearch.JuegoGato()
        k = 0
        self.actualizar_tablero()

    def actualizar_tablero(self):
        k = 0
        for i in range(6):
            fila=[]
            for j in range(6):
                if (self.juego.tablero[k] == 0):
                    b1=Button(self.principal,image=self.vacio,width="80",height="80")
                elif (self.juego.tablero[k] == 1):
                    b1 = Button(self.principal, image=self.raton, width="80", height="80")
                elif (self.juego.tablero[k] == -1):
                    b1 = Button(self.principal, image=self.gato, width="80", height="80")
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
                messagebox.showinfo("Juego del Gato", "Has ganado!")
            elif self.juego.ganador == 0:
                messagebox.showinfo("Juego del Gato", "Empate")
            else:
                messagebox.showinfo("Juego del Gato", "Has perdido")
            aisearch.JuegoGato.reiniciar(self.juego)
            self.actualizar_tablero()           
            return True
        else:
            return False

    def click(self,evento):
        ficha_jugador = evento.widget.x * 6 + evento.widget.y
        if self.juego.tablero[ficha_jugador]==0:
            jugadas_posibles = self.juego.generar_jugadas_posibles()
            ficha_jugador = ficha_jugador
            if len(jugadas_posibles) != 0:
                if ficha_jugador in jugadas_posibles:
                    self.juego.jugar(ficha_jugador)
                    print(self.juego.voltearFichas())
                    self.actualizar_tablero()
                    j = 6
                    for i in range(6):
                        print(self.juego.tablero[j-6:j])
                        j += 6
                    if not self.victoria():
                        o=[]
                        m = aisearch.alfabeta2(10, self.juego, 1,-1000, 1000, [], o)
                        print (m)
                        self.juego.jugar(m[1])
                        self.actualizar_tablero()
                        self.victoria()
            if len(jugadas_posibles) == 0:
                self.juego.jugador = -1
                if not self.victoria():
                    o=[]
                    m = aisearch.alfabeta2(10, self.juego, 1,-1000, 1000, [], o)
                    if len(m) == 2:
                        print (m)
                        self.juego.jugar(m[1])
                        self.actualizar_tablero()
                        self.victoria()
            else:
                self.victoria()           
        j = 6
        for i in range(6):
            print(self.juego.tablero[j-6:j])
            j += 6
juego=Gato()
mainloop()
