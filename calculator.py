from tkinter import Tk,Entry,Button,StringVar


class Calculator:
    def __init__(self,master):
        master.tittle("Calculator")
        master.geometry("357*420)+0+0")
        master.config(bg="blue")
        master.resizable(False,False) 

        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17,bg="powder blue",font=("arial",20,"bold"),textvariable=self.equation).place(x=0,y=0)

    def show(self.value):
          

root=Tk()
root.mainloop()
