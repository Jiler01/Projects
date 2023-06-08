from tkinter import *

morceau1="mchifreprefestle"
morceau2=2
sephra = morceau2+morceau1

texte = sephra

window = Tk()
window.title = ("Sortie du programme")
label = Label(window, text=texte, font=("3Arial",50))
label.pack(expand=YES)
window.mainloop()