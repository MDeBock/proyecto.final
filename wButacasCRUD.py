from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.Butacas as but


class Bcrud(Toplevel):
    def __init__(self, master=None, select_id = None):
        super().__init__(master)        
        self.master = master
        self.select_id = select_id     
        self.title("BUTACAS")        
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
        GLabel_464["text"] = "BUTACAS"
        GLabel_464.place(x= 300,y=10,width=200,height=40)

        tv = ttk.Treeview(self, columns=("FILA", "SILLA", "ESTADO"), name="tvButacas")
        tv.column("#0", width=78)
        tv.column("FILA", width=150, anchor=CENTER)
        tv.column("SILLA", width=150, anchor=CENTER)        
        tv.column("ESTADO", width=150, anchor=CENTER)
        
        tv.heading("#0", text="ID", anchor=CENTER)
        tv.heading("FILA", text="FILA", anchor=CENTER)
        tv.heading("SILLA", text="SILLA", anchor=CENTER)        
        tv.heading("ESTADO", text="ESTADO", anchor=CENTER)
        tv.place(x=10,y=50,width=780,height=300)          
        
        self.refrescar()
        
        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"   
        ft = tkFont.Font(family='Times',size=10)     
        btn_salir["font"] = ft
        btn_salir["fg"] = "#000000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "SALIR"
        btn_salir.place(x=690,y=360,width=100,height=30)
        btn_salir["command"] = self.salir 
            
    def salir(self):
        self.destroy()    

    def refrescar(self):        
        tvbutacas = self.nametowidget("tvButacas")
        for record in tvbutacas.get_children():
            tvbutacas.delete(record)
        butacas = but.listar()
        for butaca in butacas:
            tvbutacas.insert("", END, text=butaca[0], values=(butaca[1], butaca[2], butaca[3]))  