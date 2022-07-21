from importlib.resources import open_binary
from tkinter import *
from tkinter import ttk
import tkinter


def PrintThing():
    print(f"Button Pressed")

def open_popup():
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()

#Code For First option
bublyimage1 = tkinter.PhotoImage(file='bubly_Rasp_12.png')
ttk.Label(frm,text="Bubly Option 1",font=("Arial",25)).grid(column=1,row=0)
ttk.Button(frm, image=bublyimage1, command=open_popup).grid(column=1, row=1)

#Code for second option
bublyimage2 = tkinter.PhotoImage(file='bubly_Straw.png')
ttk.Label(frm,text="Bubly Option 2",font=("Arial",25)).grid(column=2,row=0)
ttk.Button(frm, image=bublyimage2, command=open_popup).grid(column=2, row=1)

#Code for third option
ttk.Label(frm,text="Option 3",font=("Arial",25)).grid(column=3,row=0)
ttk.Button(frm,image=bublyimage1, command=open_popup).grid(column=3, row=1)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=3)
root.mainloop()