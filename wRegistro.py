import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("REGISTRO")
        #setting window size
        width=600
        height=340
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_692=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "right"
        GLabel_692["text"] = "NOMBRE"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "APELLIDO"
        GLabel_458.place(x=0,y=60,width=200,height=30)

        GLabel_338=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_338["font"] = ft
        GLabel_338["fg"] = "#333333"
        GLabel_338["justify"] = "right"
        GLabel_338["text"] = "E-MAIL"
        GLabel_338.place(x=0,y=100,width=200,height=30)

        GLabel_251=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_251["font"] = ft
        GLabel_251["fg"] = "#333333"
        GLabel_251["justify"] = "right"
        GLabel_251["text"] = "USUARIO"
        GLabel_251.place(x=0,y=140,width=200,height=30)

        GLabel_219=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_219["font"] = ft
        GLabel_219["fg"] = "#333333"
        GLabel_219["justify"] = "right"
        GLabel_219["text"] = "CONTRASEÑA"
        GLabel_219.place(x=0,y=180,width=200,height=30)

        GLineEdit_794=tk.Entry(root)
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = "Entry"
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        GLineEdit_522=tk.Entry(root)
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = "Entry"
        GLineEdit_522.place(x=220,y=60,width=320,height=30)

        GLineEdit_570=tk.Entry(root)
        GLineEdit_570["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_570["font"] = ft
        GLineEdit_570["fg"] = "#333333"
        GLineEdit_570["justify"] = "center"
        GLineEdit_570["text"] = "Entry"
        GLineEdit_570.place(x=220,y=100,width=320,height=30)

        GLineEdit_690=tk.Entry(root)
        GLineEdit_690["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_690["font"] = ft
        GLineEdit_690["fg"] = "#333333"
        GLineEdit_690["justify"] = "center"
        GLineEdit_690["text"] = "Entry"
        GLineEdit_690.place(x=220,y=140,width=320,height=30)

        GLineEdit_43=tk.Entry(root)
        GLineEdit_43["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_43["font"] = ft
        GLineEdit_43["fg"] = "#333333"
        GLineEdit_43["justify"] = "center"
        GLineEdit_43["text"] = "Entry"
        GLineEdit_43.place(x=220,y=180,width=320,height=30)
        GLineEdit_43["show"] = "*"

        GLineEdit_210=tk.Entry(root)
        GLineEdit_210["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_210["font"] = ft
        GLineEdit_210["fg"] = "#333333"
        GLineEdit_210["justify"] = "center"
        GLineEdit_210["text"] = "Entry"
        GLineEdit_210.place(x=220,y=220,width=320,height=30)
        GLineEdit_210["show"] = "*"
        

        GLabel_170=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_170["font"] = ft
        GLabel_170["fg"] = "#333333"
        GLabel_170["justify"] = "right"
        GLabel_170["text"] = "CONFIRMAR CONTRASEÑA"
        GLabel_170.place(x=0,y=220,width=200,height=30)

        GButton_271=tk.Button(root)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=260,width=150,height=30)
        GButton_271["command"] = self.GButton_271_command

        GButton_71=tk.Button(root)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=260,width=150,height=30)
        GButton_71["command"] = self.GButton_71_command

    def GButton_271_command(self):
        print("CANCELAR")


    def GButton_71_command(self):
        print("ACEPTAR")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
