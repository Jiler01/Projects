from tkinter import *

morceau1="mchifreprefestle"
morceau2= str(2)
phrase = morceau2+morceau1

texte = phrase

window = Tk()
window.title = ("Sortie du programme")
label = Entry(window, font=("3Arial",50))
label.insert(0,texte)
label.pack(expand=YES)
window.mainloop()