import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.Peliculas as FPeliculas

class Pelicula(tk.Toplevel):
    def __init__(self, master = None, peli_id = None):
        super().__init__(master)
        self.master = master
        self.peli_id = peli_id        
        self.title("PELICULAS")        
        width=600
        height=260
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_692=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "right"
        GLabel_692["text"] = "NOMBRE"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "CLASID"
        GLabel_458.place(x=0,y=60,width=200,height=30)
        
        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "GENERO"
        GLabel_458.place(x=0,y=100,width=200,height=30)
        
        GLabel_459=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["justify"] = "right"
        GLabel_459["text"] = "PRECIO"
        GLabel_459.place(x=0,y=140,width=200,height=30)

        GLabel_460=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_460["font"] = ft
        GLabel_460["fg"] = "#333333"
        GLabel_460["justify"] = "right"
        GLabel_460["text"] = "DURACION"
        GLabel_460.place(x=0,y=180,width=200,height=30)     
        
        
        GLineEdit_794=tk.Entry(self, name="txtNombre")
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        # GLineEdit_522=tk.Entry(self, name="txtClasid")
        # GLineEdit_522["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # GLineEdit_522["font"] = ft
        # GLineEdit_522["fg"] = "#333333"
        # GLineEdit_522["justify"] = "center"
        # GLineEdit_522["text"] = ""
        # GLineEdit_522.place(x=220,y=60,width=320,height=30)  
        
        clasid = dict(FPeliculas.listar_clasid())
        cb_clasid = ttk.Combobox(self, values=list(clasid.values()), name="cbClasid")
        cb_clasid.place(x=220,y=60,width=320,height=30)
        
        GLineEdit_523=tk.Entry(self, name="txtGenero")
        GLineEdit_523["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_523["font"] = ft
        GLineEdit_523["fg"] = "#333333"
        GLineEdit_523["justify"] = "center"
        GLineEdit_523["text"] = ""
        GLineEdit_523.place(x=220,y=100,width=320,height=30) 
        
        GLineEdit_524=tk.Entry(self, name="txtPrecio")
        GLineEdit_524["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_524["font"] = ft
        GLineEdit_524["fg"] = "#333333"
        GLineEdit_524["justify"] = "center"
        GLineEdit_524["text"] = ""
        GLineEdit_524.place(x=220,y=140,width=320,height=30) 
        
        GLineEdit_525=tk.Entry(self, name="txtDuracion")
        GLineEdit_525["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_525["font"] = ft
        GLineEdit_525["fg"] = "#333333"
        GLineEdit_525["justify"] = "center"
        GLineEdit_525["text"] = ""
        GLineEdit_525.place(x=220,y=180,width=320,height=30)   
                       
        GButton_71=tk.Button(self)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=220,width=150,height=30)
        GButton_71["command"] = self.aceptar
        
        GButton_271=tk.Button(self)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=220,width=150,height=30)
        GButton_271["command"] = self.cancelar
        
        if peli_id is not None:
            peli = FPeliculas.obtener_id(peli_id)
            if peli is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la Pelicula, reintente nuevamente")
               self.destroy()
            else:                
                GLineEdit_794.insert(0, peli[1])
                cb_clasid.set(peli[2])
                GLineEdit_523.insert(0, peli[3])
                GLineEdit_524.insert(0, peli[4]) 
                GLineEdit_525.insert(0, peli[5])
                                                      
                
    
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1  


    def cancelar(self):
        self.destroy()  
                
    def aceptar(self):
        try:            
            nombre = self.get_value("txtNombre")
            clasid = self.get_value("cbClasid")
            genero = self.get_value("txtGenero")
            precio = self.get_value("txtPrecio")
            duracion = self.get_value("txtDuracion")

            if nombre =="":
                tkMsgBox.showerror(self.master.title(), "Nombre es un valor requerido.")
                return 
            if clasid =="":
                tkMsgBox.showerror(self.master.title(), "Clasificación es un valor requerido.")
                return  
            if genero =="":
                tkMsgBox.showerror(self.master.title(), "Genero es un valor requerido.")
                return  
            if precio =="":
                tkMsgBox.showerror(self.master.title(), "Precio es un valor requerido.")
                return 
            if duracion =="":
                tkMsgBox.showerror(self.master.title(), "Duración es un valor requerido.")
                return
                
            if self.peli_id is None:                                  
                FPeliculas.agregar(nombre, clasid, genero, precio, duracion)
                tkMsgBox.showinfo(self.master.title(), "Pelicula agregada!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()  
            else:
                print("Actualizacion de pelicula")
                FPeliculas.actualizar(nombre, clasid, genero, precio, duracion, self.peli_id)  
                tkMsgBox.showinfo(self.master.title(), "Pelicula modificada!!!!!!")                
                self.master.refrescar()
                self.destroy()      
                
                
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))