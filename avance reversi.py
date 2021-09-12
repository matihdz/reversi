from tkinter import *
from tkinter import messagebox
from functools import partial


ventana = Tk()
ventana.geometry("300x500")

listaEntradas = []

class Persona():
    def __init__(self, nombre, apellido, rut, sexo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.sexo = sexo
        self.edad = edad
    
    def saludo(self):
        greetings = "Hola, soy " + self.nombre + ", tengo " + self.edad + " años y soy de sexo " + self.sexo + "."
        return greetings

class Alumno(Persona):
    def __init__(self, nombre, apellido, rut, sexo, edad, colegio, curso):
        super().__init__(nombre, apellido, rut, sexo, edad)
        self.colegio = colegio
        self.curso = curso


def crear_Alumno(nombre, apellido, rut, sexo, edad, colegio, curso):
    nuevo_alumno = Alumno(nombre, apellido, rut, sexo, edad, colegio, curso)
    listaEntradas.append(nuevo_alumno)
    ventana2 = Tk()
    ventana2.geometry("200x250")
    textoEtiqueta = nuevo_alumno.saludo()
    etiqueta = Label(ventana2, text = textoEtiqueta)
    boton2 = Button(ventana2, text = 'Añadir otro alumno', padx = 20, pady = 20, command = ventana2.destroy)
    etiqueta.pack()
    boton2.pack()


caja_nombre = Entry(ventana)
caja_apellido = Entry(ventana)
caja_rut = Entry(ventana)
caja_sexo = Entry(ventana)
caja_edad = Entry(ventana)
caja_colegio = Entry(ventana)
caja_curso = Entry(ventana)

caja_nombre.pack()
caja_apellido.pack()
caja_rut.pack()
caja_sexo.pack()
caja_edad.pack()
caja_colegio.pack()
caja_curso.pack()

boton1 = Button(ventana, text = 'uwu', padx = 20, pady = 20, command = lambda: crear_Alumno(caja_nombre.get(), caja_apellido.get(), caja_rut.get(), caja_sexo.get(), caja_edad.get(), caja_colegio.get(), caja_curso.get()))
boton2 = Button(ventana, text = 'lista', padx = 20, pady = 20, command = lambda: print(listaEntradas.nombre))
boton1.pack()
boton2.pack()

'''ventana.mainloop()'''





class Reversi:
    def __init__(self):
        self.tablero = Tk()
        self.tablero.title("Reversi")
        self.tablero.geometry("516x600")
        self.botones = []
        self.negra = PhotoImage(file = r'C:\Users\Erick\Documents\Projects\reversi\usuario.png', master = self.tablero)
        self.blanca = PhotoImage(file = r'C:\Users\Erick\Documents\Projects\reversi\agente.png', master = self.tablero)
        self.vacia = PhotoImage(file = r'C:\Users\Erick\Documents\Projects\reversi\vacio.png', master = self.tablero)
        for i in range(6):
            fila = []
            for j in range(6):
                b1= Button(self.tablero, image = self.vacia, width="80", height="80")
                b1.x = i
                b1.y = j
                b1.grid(row = i, column = j)
                fila.append(b1)
            self.botones.append(fila)
        self.puntaje = Label(self.tablero, text = "00 00", font = ('Arial', 25))
        self.puntaje.grid(row = 6, column = 5)

    
    def victoria(self):
        if self.juego.estado_final == 1:
            messagebox.showinfo("Has ganado el Reversi")
        elif self.juego.ganador == 0:
            messagebox.showinfo("Has empatado el Reversi")
        else:
            messagebox.showinfo("Has perdido el Reversi")
        self.juego.reiniciar()
        for i in range(6):
            for j in range(6):
                self.botones[i][j]["image"] = self.vacia
    
    def actualizarPtje(self):
        pass




reverso = Reversi()
mainloop()
