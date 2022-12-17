from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.Salas as salasf
from wSalas import Sala
from wButacasCRUD import Bcrud



class Scrud(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("SALAS")        
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
        GLabel_464["text"] = "SALAS"
        GLabel_464.place(x= 350,y=10,width=100,height=40)

        tv = ttk.Treeview(self, columns=("N_SALA", "FORMATO", "CAPACIDAD",), name="tvSalas")
        tv.column("#0", width=78)
        tv.column("N_SALA", width=100, anchor=CENTER)
        tv.column("FORMATO", width=150, anchor=CENTER)
        tv.column("CAPACIDAD", width=150, anchor=CENTER)      
        
        tv.heading("#0", text="ID", anchor=CENTER)
        tv.heading("N_SALA", text="N_SALA", anchor=CENTER)
        tv.heading("FORMATO", text="FORMATO", anchor=CENTER)
        tv.heading("CAPACIDAD", text="CAPACIDAD", anchor=CENTER)        
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=50,width=780,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_verButacas = Button(self)
        btn_verButacas["bg"] = "#f0f0f0"        
        btn_verButacas["font"] = ft
        btn_verButacas["fg"] = "#000000"
        btn_verButacas["justify"] = "center"
        btn_verButacas["text"] = "VER BUTACAS"
        btn_verButacas.place(x=10,y=360,width=100,height=30)
        btn_verButacas["command"] = self.verButacas

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
        salas = self.nametowidget("tvSalas")
        current_item = salas.focus()
        if current_item:
            data = salas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Sala(self)

    def editar(self): 
        Sala(self, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            salasf.eliminar(self.select_id)
            self.refrescar()

    def verButacas(self):
        Bcrud(self, self.select_id)
        
           
    def salir(self):
        self.destroy()
    
    def refrescar(self):        
        tvSalas = self.nametowidget("tvSalas")
        for record in tvSalas.get_children():
            tvSalas.delete(record)
        salas = salasf.listar()
        for sala in salas:
            tvSalas.insert("", END, text=sala[0], values=(sala[1], sala[2], sala[3])) 