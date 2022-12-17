from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.Peliculas as peli
from wpelicula import Pelicula

class Pcrud(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("PELICULAS")        
        width=800
        height=400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "PELICULAS"
        GLabel_464.place(x= 300,y=10,width=200,height=40)

        tv = ttk.Treeview(self, columns=("NOMBRE", "GENERO", "DURACION", "APTO", "PRECIO" ), name="tvPeliculas")
        tv.column("#0", width=50)
        tv.column("NOMBRE", width=250, anchor=CENTER)
        tv.column("GENERO", width=100, anchor=CENTER)
        tv.column("DURACION", width=100, anchor=CENTER)
        tv.column("APTO", width=100, anchor=CENTER)
        tv.column("PRECIO", width=100, anchor=CENTER)
        
        tv.heading("#0", text="ID", anchor=CENTER)
        tv.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
        tv.heading("GENERO", text="GENERO", anchor=CENTER)
        tv.heading("DURACION", text="DURACION", anchor=CENTER)
        tv.heading("APTO", text="APTO", anchor=CENTER)
        tv.heading("PRECIO", text="PRECIO", anchor=CENTER)     
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=50,width=780,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "NUEVA"
        btn_agregar.place(x=360,y=360,width=100,height=30)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "EDITAR"
        btn_editar.place(x=470,y=360,width=100,height=30)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "ELIMINAR"
        btn_eliminar.place(x=580,y=360,width=100,height=30)
        btn_eliminar["command"] = self.eliminar
        
        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#000000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "SALIR"
        btn_salir.place(x=690,y=360,width=100,height=30)
        btn_salir["command"] = self.salir
        
    def obtener_fila(self, event):
        tvPeliculas = self.nametowidget("tvPeliculas")
        current_item = tvPeliculas.focus()
        if current_item:
            data = tvPeliculas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Pelicula(self)

    def editar(self): 
        Pelicula(self, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.title(), "¿Está seguro de eliminar esta Pelicula?")   
        if answer:
            peli.eliminar(self.select_id)
            self.refrescar()
            
    def salir(self):
        self.destroy()
    
    def refrescar(self):        
        tvPeliculas = self.nametowidget("tvPeliculas")
        for record in tvPeliculas.get_children():
            tvPeliculas.delete(record)
        peliculas = peli.listar()
        for movie in peliculas:
            tvPeliculas.insert("", END, text=movie[0], values=(movie[1], movie[2], movie[3], movie[4], movie[5])) 