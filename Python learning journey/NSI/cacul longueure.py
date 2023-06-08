from tkinter import *


def exec():
    phrase = phentr.get()
    #x = xentr.get()
    texte.set(("Caractères: " +str(len(phrase)) +"\nSoit deux morceaux de : " +str((len(phrase)/2))))

    
    
window = Tk()
texte = StringVar()
window.geometry ("1800x780")
window.title ("Sortie du programme")
label = Label(window, font=("Arial",10), justify="center",textvariable=texte)

button = Button(window,text="Entrer",command=exec)
xentr = Entry(window, font=("Arial",25), justify="center")
phentr = Entry(window, font=("Arial",25,), justify="center")
xq = Label(window, font=("Arial",25), justify="center",text= "x = ?")
stq = Label(window, font=("Arial",25), justify="center",text= "str = ?")

label.pack(fill=X,expand=YES)
button.pack(fill=X,expand=YES)
stq.pack(fill=X,expand=YES)
phentr.pack(fill=X,expand=YES)
#xq.pack(fill=X,expand=YES)
#xentr.pack(fill=X,expand=YES)

    
window.mainloop()