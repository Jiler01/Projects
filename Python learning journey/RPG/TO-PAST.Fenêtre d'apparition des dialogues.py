from tkinter import *
from time import *
printime2 = 0

def printt (*textargs):
    textvar2 = str()
    for textarg in textargs:
        textvar2 = textvar2 + " "+ str(textarg)
    textvar.set(textvar2)

def prrint (printime,*printext):
    global printime2
    root.after(printime2*1000, lambda: printt(*printext))
    printime2 = printime

#Nouvelle fenetre
root = Tk()
root.geometry ("480x270")
root.resizable(0,0)
root.title ("RPG")

#Nouveau label d'apparition des dialogues
textvar = StringVar()
label = Label(root, font=("Arial",12),textvariable=textvar)

#Empaquetage
label.pack(fil=BOTH,expand=YES)

prrint(3,"123456789",3,3,"dfghj")
prrint(0,"98765432")


root.mainloop()