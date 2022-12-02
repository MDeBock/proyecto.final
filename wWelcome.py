import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("WELCOME TO CINEMARC")
        #setting window size
        width=500
        height=100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_898=tk.Button(root)
        GButton_898["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_898["font"] = ft
        GButton_898["fg"] = "#000000"
        GButton_898["justify"] = "center"
        GButton_898["text"] = "BIENVENIDOS A CINEMARC"       
        GButton_898.place(x=0,y=0,width=500,height=100)
        GButton_898["command"] = self.GButton_898_command

    def GButton_898_command(self):
        print("BIENVENIDOS A CINEMARC")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
