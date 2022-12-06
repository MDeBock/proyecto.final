import tkinter as tk
import tkinter.font as tkFont
from wRegistro import Registro
import tkinter.messagebox as tkMsgBox
from wAdm import Adm

class Login(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("LOGIN")
        #setting window size
        width=450
        height=170
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_663=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_663["font"] = ft
        GLabel_663["fg"] = "#333333"
        GLabel_663["justify"] = "right"
        GLabel_663["text"] = "USUARIO"
        GLabel_663.place(x=0,y=20,width=100,height=30)

        GLabel_886=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_886["font"] = ft
        GLabel_886["fg"] = "#333333"
        GLabel_886["justify"] = "right"
        GLabel_886["text"] = "CONTRASEÑA"
        GLabel_886.place(x=0,y=60,width=100,height=30)

        GButton_750=tk.Button(self)
        GButton_750["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_750["font"] = ft
        GButton_750["fg"] = "#000000"
        GButton_750["justify"] = "center"
        GButton_750["text"] = "REGISTRARSE"
        GButton_750.place(x=10,y=120,width=100,height=30)
        GButton_750["command"] = self.registro

        GButton_630=tk.Button(self)
        GButton_630["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_630["font"] = ft
        GButton_630["fg"] = "#000000"
        GButton_630["justify"] = "center"
        GButton_630["text"] = "ENTRAR"
        GButton_630.place(x=200,y=120,width=100,height=30)
        GButton_630["command"] = self.entrar #self.GButton_630_command

        GButton_638=tk.Button(self)
        GButton_638["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_638["font"] = ft
        GButton_638["fg"] = "#000000"
        GButton_638["justify"] = "center"
        GButton_638["text"] = "CANCELAR"
        GButton_638.place(x=340,y=120,width=100,height=30)
        GButton_638["command"] = self.cancelar

        GLineEdit_134=tk.Entry(self)
        GLineEdit_134["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_134["font"] = ft
        GLineEdit_134["fg"] = "#333333"
        GLineEdit_134["justify"] = "center"
        GLineEdit_134["text"] = ""
        GLineEdit_134.place(x=120,y=20,width=320,height=30)

        GLineEdit_150=tk.Entry(self)
        GLineEdit_150["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_150["font"] = ft
        GLineEdit_150["fg"] = "#333333"
        GLineEdit_150["justify"] = "center"
        GLineEdit_150["text"] = ""
        GLineEdit_150.place(x=120,y=60,width=320,height=30)
        GLineEdit_150["show"] = "*"
        
    #TODO    
    # def iniciar_sesion(self):
    #     try:
    #         txtUsuario = self.nametowidget("txtUsuario")
    #         usuario = txtUsuario.get()            

    #         txtContrasenia = self.nametowidget("txtContrasenia")
    #         contrasenia = txtContrasenia.get()

    #         if usuario != "":
    #             if user.validar(usuario, contrasenia):
    #                 Dashboard(self.master)
    #                 self.destroy()
    #             else:
    #                 tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
    #         else:
    #             tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
    #     except Exception as ex:
    #         tkMsgBox.showerror(self.master.title(), str(ex))

    def registro(self):
        Registro(self.master)
    
    def entrar(self):
        Adm(self.master)


    def GButton_630_command(self):
        print("ENTRAR")


    def cancelar(self):
        self.destroy()

# if __name__ == "__main__":
#     self = tk.Tk()
#     self.iconbitmap(default="cinemark.ico")
#     app = Login(self)
#     self.mainloop()


