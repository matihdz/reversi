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
        aj = None
        print(self.juego.tablero)
        if self.juego.tablero[evento.widget.x * 6 + evento.widget.y]==0:
            '''jugadasPosibles = self.juego.generar_jugadas_posibles()
            if self.juego in jugadasPosibles:'''
            self.juego.jugar(evento.widget.x * 6 + evento.widget.y)
            self.actualizar_tablero()
            if not self.victoria():
                o=[]
                m=aisearch.alfabeta(10, self.juego, 1,-1000, 1000, [], o)
                print (m)
                self.juego.jugar(m[1])
                self.actualizar_tablero()
                self.victoria()
                aj = self.juego.voltearF(m[1])
                print (aj)
        print(self.juego.tablero)
juego=Gato()
mainloop()
