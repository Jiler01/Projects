from tkinter import *
root = Tk()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()

#------------------------------Les Variables------------------------------#
projectname = "Retourner chaine"
police = ("Arial",40)

text1.set("")
text2.set("Phrase ?")
text3.set("")


button1text = "Retourner"
button2text = ""
button3text = ""
#------------------------------Les Variables------------------------------#

root.title(projectname)
root.geometry("900x700")
texte1=Label(root,font=(police),textvariable=text1, justify="center")
texte2=Label(root,font=(police),textvariable=text2, justify="center")
texte3=Label(root,font=(police),textvariable=text3, justify="center")
input1 = Entry(root,font=(police), justify="center")
input2 = Entry(root,font=(police), justify="center")
input3 = Entry(root,font=(police), justify="center")



#------------------------------Les Fonctions------------------------------#
def exec1():
    global i
    global motr
    i = 0
    motr = ""
    def returnn(mot):
        global i
        global motr
        if i == len(mot):
            return(motr)
        else:
            motr = motr + mot[(len(mot)-(i+1))]
            i = i+1
            returnn(mot)

    returnn(input2.get())
    text1.set(returnn(input2.get()))



def exec2():
    print()

def exec3():
    print()
#------------------------------Les Fonctions------------------------------#



button1 = Button(root, text=button1text, font=(police), command=exec1, justify="center")
button2 = Button(root, text=button2text, font=(police), command=exec2, justify="center")
button3 = Button(root, text=button3text, font=(police), command=exec3, justify="center")



#------------------------------Empaquetage------------------------------#
texte1.pack()
button1.pack()
#input1.pack()
texte2.pack()
input2.pack()
#texte3.pack()
#input3.pack()
#button2.pack()
#button3.pack()
#------------------------------Empaquetage------------------------------#


root.mainloop()