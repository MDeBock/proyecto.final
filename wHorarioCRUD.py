from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.horarios as hor
from wHorarios import Horario

class Hcrud(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("HORARIOS")        
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
        GLabel_464["text"] = "HORARIOS"
        GLabel_464.place(x= 350,y=10,width=100,height=40)

        tv = ttk.Treeview(self, columns=("FECHA", "HORA", "PELICULA", "N_SALA"), name="tvHorarios")
        tv.column("#0", width=78)
        tv.column("FECHA", width=100, anchor=CENTER)
        tv.column("HORA", width=150, anchor=CENTER)
        tv.column("PELICULA", width=150, anchor=CENTER)
        tv.column("N_SALA", width=150, anchor=CENTER)


        tv.heading("#0", text="ID", anchor=CENTER)
        tv.heading("FECHA", text="FECHA", anchor=CENTER)
        tv.heading("HORA", text="HORA", anchor=CENTER)
        tv.heading("PELICULA", text="PELICULA", anchor=CENTER)
        tv.heading("N_SALA", text="N_SALA", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=50,width=780,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "AGREGAR"
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
        tvhorarios = self.nametowidget("tvHorarios")
        current_item = tvhorarios.focus()
        if current_item:
            data = tvhorarios.item(current_item)
            print(data["text"])
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Horario(self)

    def editar(self):
        Horario(self, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.title(), "¿Está seguro de eliminar esta Funcion?")   
        if answer:
            hor.eliminar(self.select_id)
            self.refrescar()
            
    def salir(self):
        self.destroy()        
    
    def refrescar(self):        
        tvhorarios = self.nametowidget("tvHorarios")
        for record in tvhorarios.get_children():
            tvhorarios.delete(record)
        horarios = hor.listar()
        for horario in horarios:
            tvhorarios.insert("", END, text=horario[0], values=(horario[1], horario[2], horario[3], horario[4])) 