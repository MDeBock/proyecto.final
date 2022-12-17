import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.horarios as hor
import bll.Peliculas as Peliculas
import bll.Salas as Salas


class Horario(tk.Toplevel):
    def __init__(self, master = None, h_id = None):
        super().__init__(master)
        self.master = master
        self.h_id = h_id        
        self.title("FUNCIONES")        
        width=600
        height=220
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
        GLabel_692["text"] = "FECHA"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "HORA"
        GLabel_458.place(x=0,y=60,width=200,height=30)
        
        GLabel_693=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_693["font"] = ft
        GLabel_693["fg"] = "#333333"
        GLabel_693["justify"] = "right"
        GLabel_693["text"] = "PELICULA"
        GLabel_693.place(x=0,y=100,width=200,height=30)

        GLabel_459=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["justify"] = "right"
        GLabel_459["text"] = "SALA"
        GLabel_459.place(x=0,y=140,width=200,height=30)
        
        GLineEdit_794=tk.Entry(self, name="txtFecha")
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        GLineEdit_522=tk.Entry(self, name="txtHora")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=220,y=60,width=320,height=30)
        
        pelicula = dict(Peliculas.listar_peli())
        cb_pelicula = ttk.Combobox(self, values=list(pelicula.values()), name="cbPelicula")
        cb_pelicula.place(x=220,y=100,width=320,height=30)
        
        sala = dict(Salas.listar_sala())
        cb_sala = ttk.Combobox(self, values=list(sala.values()), name="cbSala")
        cb_sala.place(x=220,y=140,width=320,height=30)
                
        GButton_71=tk.Button(self)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=180,width=150,height=30)
        GButton_71["command"] = self.aceptar
        
        GButton_271=tk.Button(self)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=180,width=150,height=30)
        GButton_271["command"] = self.cancelar
        
        if h_id is not None:
            hs = hor.obtener_id(h_id)
            if hs is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de funciones, reintente nuevamente")
               self.destroy()
            else:                
                GLineEdit_794.insert(0, hs[1])
                GLineEdit_522.insert(0, hs[2])
                cb_pelicula.set(hs[3])
                cb_sala.set(hs[4])  
           
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1  


    def cancelar(self):
        self.destroy()
    
        
    def aceptar(self):
        try:            
            fecha = self.get_value("txtFecha")
            hora = self.get_value("txtHora")
            pelicula = self.get_value("cbPelicula") 
            sala = self.get_value("cbSala")
            
            if self.h_id is None:           
                hor.agregar(fecha, hora, pelicula, sala)
                tkMsgBox.showinfo(self.master.title(), "Funcion agregada!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()  
            else:
                print("Actualizacion de horario")                
                hor.actualizar(fecha, hora, pelicula, sala, self.h_id)  
                tkMsgBox.showinfo(self.master.title(), "Funcion modificada!!!!!!")                
                self.master.refrescar()
                self.destroy()      
                
                
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))
            
            

