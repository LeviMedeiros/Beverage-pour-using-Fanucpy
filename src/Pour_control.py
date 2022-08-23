#Import multiprocessing library
import imp
import multiprocessing
from multiprocessing import Process
from multiprocessing.connection import wait

#Import GUI library
import tkinter
from tkinter import *
from tkinter import ttk

#import sleep timer
import time

#Import Files that contain the routines for each robot
from Right_Bot_Routine import right_bot_rountine
from Left_Bot_Routine import left_bot_routine

#Declare variables used to change routine per beverage selection
global maxspeed
global maxaccel

maxspeed = 100
maxaccel = 100
    
def callRoutines(routine):
    #Initializing the multiprocessing
    if __name__ == '__main__':
        #Set up events for syncronization
        leftset = multiprocessing.Event()
        rightset = multiprocessing.Event()
            
        #Pop Up in progress Window
        inProgress = Toplevel(root)
        inProgress.geometry("750x250")
        inProgress.title("Pouring in Progress")
        Label(inProgress, text= "Pouring in progress", font=('Mistral 18 bold')).place(x=150,y=80)
        inProgress.focus_set()

        #Set up the processes
        p1 = multiprocessing.Process(target = left_bot_routine, args= (routine,leftset,rightset))
        p2 = multiprocessing.Process(target = right_bot_rountine, args= (routine,leftset,rightset))
        #Start the processes
        p1.start()
        p2.start()
        #Wait for the processes to finish
        p1.join()
        p2.join()
        #Close the in progress window
        inProgress.destroy()
    
#functions to select the routine
def callroutine1():
    callRoutines(1)

def callroutine2():
    callRoutines(2)

def callroutine3():
    callRoutines(3)

#Setup GUI
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

#Code For First option, When button is pressed callroutine1() is run
Option1Image = tkinter.PhotoImage(file='Tall_CAN.png')
ttk.Label(frm,text="Regular Beer",font=("Arial",25)).grid(column=1,row=0)
ttk.Button(frm, image=Option1Image, command=callroutine1).grid(column=1, row=1)

#Code for second option, When button is pressed callroutine2() is run
Option2Image = tkinter.PhotoImage(file='Small Can.png')
ttk.Label(frm,text="Pop and Bubly",font=("Arial",25)).grid(column=2,row=0)
ttk.Button(frm, image=Option2Image, command=callroutine2).grid(column=2, row=1)

#Code for third option, When button is pressed callroutine3() is run
Option3Image = tkinter.PhotoImage(file='Tall_CAN.png')
ttk.Label(frm,text="Tall Beer",font=("Arial",25)).grid(column=3,row=0)
ttk.Button(frm,image=Option3Image, command=callroutine3).grid(column=3, row=1)

#Code to have exit button in bottom right
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=3)

#Use GUI
if __name__=='__main__':
    root.mainloop()



