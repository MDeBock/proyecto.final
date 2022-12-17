import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.Salas as FSalas



class Sala(tk.Toplevel):
    def __init__(self, master = None, sala_id = None):
        super().__init__(master)
        self.master = master
        self.sala_id = sala_id        
        self.title("SALAS")        
        width=600
        height=180
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_692=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "right"
        GLabel_692["text"] = "Nº_SALA"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "FORMATO"
        GLabel_458.place(x=0,y=60,width=200,height=30) 

        GLabel_459=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_459["font"] = ft
        GLabel_459["fg"] = "#333333"
        GLabel_459["justify"] = "right"
        GLabel_459["text"] = "CAPACIDAD"
        GLabel_459.place(x=0,y=100,width=200,height=30)       
        
        
        GLineEdit_794=tk.Entry(self, name="txtNº_sala")
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        GLineEdit_522=tk.Entry(self, name="txtFormato")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=220,y=60,width=320,height=30)

        GLineEdit_523=tk.Entry(self, name="txtCapacidad")
        GLineEdit_523["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_523["font"] = ft
        GLineEdit_523["fg"] = "#333333"
        GLineEdit_523["justify"] = "center"
        GLineEdit_523["text"] = ""
        GLineEdit_523.place(x=220,y=100,width=320,height=30)    
                       
        GButton_71=tk.Button(self)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=140,width=150,height=30)
        GButton_71["command"] = self.aceptar
        
        GButton_271=tk.Button(self)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=140,width=150,height=30)
        GButton_271["command"] = self.cancelar
        
        if sala_id is not None:
            sala = FSalas.obtener_id(sala_id)
            if sala is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del descuento, reintente nuevamente")
               self.destroy()
            else:                
                GLineEdit_794.insert(0, sala[0])
                GLineEdit_522.insert(0, sala[1])
                GLineEdit_523.insert(0, sala[2])                                           
                
    
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1  


    def cancelar(self):
        self.destroy()
    
        
    def aceptar(self):
        try:            
            nSala = self.get_value("txtNº_sala")
            formato = self.get_value("txtFormato")
            capacidad = self.get_value("txtCapacidad")

            if nSala =="":
                tkMsgBox.showerror(self.master.title(), "Sala es un valor requerido.")
                return
            if formato =="":
                tkMsgBox.showerror(self.master.title(), "Formato es un valor requerido.")
                return 
            if capacidad =="":
                tkMsgBox.showerror(self.master.title(), "Capacidad es un valor requerido.")
                return                        
                
            if self.sala_id is None:                                  
                FSalas.agregar(nSala, formato, capacidad)
                tkMsgBox.showinfo(self.master.title(), "Sala agregada!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()  
            else:
                print("Actualizacion de Sala")
                FSalas.actualizar(nSala, formato, capacidad, self.sala_id)  
                tkMsgBox.showinfo(self.master.title(), "Sala modificada!!!!!!")                
                self.master.refrescar()
                self.destroy()      
                
                
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))