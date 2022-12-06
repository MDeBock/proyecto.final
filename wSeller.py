import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("SELLER")
        #setting window size
        width=240
        height=130
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_561=tk.Button(root)
        GButton_561["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_561["font"] = ft
        GButton_561["fg"] = "#000000"
        GButton_561["justify"] = "center"
        GButton_561["text"] = "VENDER ENTRADA"
        GButton_561.place(x=20,y=20,width=200,height=30)
        GButton_561["command"] = self.GButton_561_command

        GButton_269=tk.Button(root)
        GButton_269["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_269["font"] = ft
        GButton_269["fg"] = "#000000"
        GButton_269["justify"] = "center"
        GButton_269["text"] = "SALIR"
        GButton_269.place(x=20,y=70,width=200,height=30)
        GButton_269["command"] = self.GButton_269_command

    def GButton_561_command(self):
        print("command")


    def GButton_269_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
