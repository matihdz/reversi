import aisearch
from tkinter import *
from tkinter import messagebox

tamanio = 3
class Gato:
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Reversi")
        self.botones=[]
        self.gato=PhotoImage(file="./resources/agente.png")
        self.raton=PhotoImage(file="./resources/usuario.png")
        self.vacio=PhotoImage(file="./resources/vacio.png")
        self.juego=aisearch.JuegoGato()
        for i in range(tamanio):
            fila=[]
            for j in range(tamanio):
                if (i == 2 and j == 2):
                    b1 = Button(self.principal, image=self.raton, width="80", height="80")
                elif (i == 2 and j == 3):
                    b1 = Button(self.principal, image=self.gato, width="80", height="80")
                elif (i == 3 and j == 2):
                    b1 = Button(self.principal, image=self.gato, width="80", height="80")
                elif (i == 3 and j == 3):
                    b1 = Button(self.principal, image=self.raton, width="80", height="80")
                else:
                    b1=Button(self.principal,image=self.vacio,width="80",height="80")
                b1.bind("<Button-1>",self.click)
                b1.x=i
                b1.y=j
                b1.grid(row=i,column=j)
                fila.append(b1)
            self.botones.append(fila)

    def victoria(self):
        if self.juego.estado_final():
            if self.juego.ganador == 1:
                messagebox.showinfo("Juego del Gato", "Has ganado!")
            elif self.juego.ganador == 0:
                messagebox.showinfo("Juego del Gato", "Empate")
            else:
                messagebox.showinfo("Juego del Gato", "Has perdido")
            self.juego.reiniciar()
            for i in range(tamanio):
                for j in range(tamanio):
                    self.botones[i][j]["image"] = self.vacio
            return True
        else:
            return False
    def click(self,evento):
        if self.juego.tablero[evento.widget.x * tamanio + evento.widget.y]==0:
            self.juego.jugar(evento.widget.x * tamanio + evento.widget.y)
            evento.widget["image"] = self.raton
            if not self.victoria():
                o=[]
                m=aisearch.alfabeta(self.juego,1,-1000,1000, [], o)
                print(m)
                #print(len(o))
                self.juego.jugar(m[1])
                self.botones[m[1]//tamanio][m[1]%tamanio]["image"]=self.gato
                self.victoria()
juego=Gato()
mainloop()
