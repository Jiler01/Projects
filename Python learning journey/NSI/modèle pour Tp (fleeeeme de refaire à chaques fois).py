from tkinter import *
from tkinter import messagebox
root = Tk()
texts = []
def texting(num,mot):
    texts.append(StringVar())
    texts[num].set(mot)
    return



#------------------------------Assignation des Variables------------------------------#
projectname = "" #nom du projet

police = ("Arial",30) #police(nom,taille)
taillefen = "-0+0" #placement de la fenetre. ici, -0=e et +0=n -> ne
nbform = 5  #nombre de formulaires demandés

buttontext = ["Bouton 0","1"] #textes des boutons (qté dans les [] = nbform)

texting(0,"Label 0") #textes des labels (rang,"texte") (qté en lignes = nbform)
#------------------------------Assignation des Variables------------------------------#


heightresult = nbform*3 #hauteur de la case résultat
widthresult = 10 #largeur de la case résultat
root.title(projectname)
root.geometry(taillefen)
root.resizable(width=False, height=False)
frame=Frame(root)
scroll=Scrollbar(root)
scroll.grid(column=3, sticky="ns")
result=Text(root,font=(police),height=heightresult, width=widthresult, yscrollcommand=scroll.set)
label=[]
input = []
button = []
for i in range(nbform):
    label.append("")
    texts.append(StringVar())
    label[i]=Label(frame,font=(police),textvariable=texts[i], justify="center")

    input.append("")
    input[i] = Entry(frame,font=(police), justify="center")

    button.append("")
    buttontext.append("")
    button[i] = Button(frame, text=buttontext[i], font=(police), justify="center")



#------------------------------Création des Fonctions------------------------------#
def exec0(): #fonction liée au bouton 0
    button[0].flash()
    result.delete("1.0","end")
    result.insert("1.0",input[0].get())
    input[0].delete(0,END)

def exec1(): #fonction liée au bouton 1
    button[1].flash()
    result.delete("1.0","end")
    messagebox.showerror("Erreur","Aucune fonction associée à ce Bouton")
    input[1].delete(0,END)

exec = [exec0,exec1] #recensement des fomctions, dans l'ordre. il nbform fonctions
#------------------------------Création des Fonctions------------------------------#



for i in range(nbform):
    exec.append("")
    button[i].configure(command=exec[i])
for i in range(nbform):
    label[i].grid()
    input[i].grid()
    button[i].grid()
frame.grid(column=0,row=0,ipady=5, padx=5)
result.grid(column=1,row=0,ipady=5, padx=5)



#------------------------------Écriture du scénario------------------------------#
messagebox.showinfo(f"Informations de Logiciel","Type : Formulaire à modifier\nAuteur : @jiler01") #ptite fenetre de debut
#------------------------------Écriture du scénario------------------------------#



root.mainloop()