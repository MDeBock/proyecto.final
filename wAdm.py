import tkinter as tk
import tkinter.font as tkFont
from wRegistro import Registro

class Adm(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("ADMIN")
        #setting window size
        width=240
        height=270
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_723=tk.Button(self)
        GButton_723["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_723["font"] = ft
        GButton_723["fg"] = "#000000"
        GButton_723["justify"] = "center"
        GButton_723["text"] = "RESERVAS"
        GButton_723.place(x=20,y=20,width=200,height=30)
        GButton_723["command"] = self.GButton_723_command

        GButton_500=tk.Button(self)
        GButton_500["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_500["font"] = ft
        GButton_500["fg"] = "#000000"
        GButton_500["justify"] = "center"
        GButton_500["text"] = "SALAS"
        GButton_500.place(x=20,y=70,width=200,height=30)
        GButton_500["command"] = self.GButton_500_command

        GButton_596=tk.Button(self)
        GButton_596["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_596["font"] = ft
        GButton_596["fg"] = "#000000"
        GButton_596["justify"] = "center"
        GButton_596["text"] = "DESCUENTOS"
        GButton_596.place(x=20,y=120,width=200,height=30)
        GButton_596["command"] = self.GButton_596_command

        GButton_852=tk.Button(self)
        GButton_852["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_852["font"] = ft
        GButton_852["fg"] = "#000000"
        GButton_852["justify"] = "center"
        GButton_852["text"] = "REGISTRO"
        GButton_852.place(x=20,y=170,width=200,height=30)
        GButton_852["command"] = self.registro
        
        GButton_724=tk.Button(self)
        GButton_724["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_724["font"] = ft
        GButton_724["fg"] = "#000000"
        GButton_724["justify"] = "center"
        GButton_724["text"] = "SALIR"
        GButton_724.place(x=20,y=220,width=200,height=30)
        GButton_724["command"] = self.salir
        
    def GButton_723_command(self):
        print("RESERVAS")


    def GButton_500_command(self):
        print("SALAS")


    def GButton_596_command(self):
        print("DESCUENTOS")
    
    def registro(self):
        Registro(self.master)


    def salir(self):
        self.destroy()


