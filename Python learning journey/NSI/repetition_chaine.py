from tkinter import *

phrase = "salut à tous!"*3

texte = phrase

window = Tk()
window.geometry ("1800x50")
window.title ("Sortie du programme")
label = Entry(window, font=("3Arial",25))
label.insert(0,texte)
label.pack(fill=X,expand=YES)
window.mainloop()