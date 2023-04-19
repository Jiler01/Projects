from tkinter import *
root = Tk()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()

#------------------------------Les Variables------------------------------#
projectname = "ASCII Decompoaer"
police = ("Arial",30)
taillefen = "900x1600"

text1.set("")
text2.set("Phrase ?")
text3.set("")


button1text = "ASCII"
button2text = ""
button3text = ""
#------------------------------Les Variables------------------------------#

root.title(projectname)
root.geometry(taillefen)
texte1=Label(root,font=(police),textvariable=text1, justify="center")
texte2=Label(root,font=(police),textvariable=text2, justify="center")
texte3=Label(root,font=(police),textvariable=text3, justify="center")
input1 = Entry(root,font=(police), justify="center")
input2 = Entry(root,font=(police), justify="center")
input3 = Entry(root,font=(police), justify="center")
button1 = Button(root, text=button1text, font=(police), justify="center")
button2 = Button(root, text=button2text, font=(police), justify="center")
button3 = Button(root, text=button3text, font=(police), justify="center")


#------------------------------Les Fonctions------------------------------#
def exec1():
    button1.flash()
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
            motr = motr + f"{mot[i]} => BIN:{bin(ord(mot[i]))[2:]} HEX:{hex(ord(mot[i]))[2:]}\n"
            i = i+1
            returnn(mot)

    returnn(input2.get())
    text1.set(returnn(input2.get()))
    input2.delete(0,END)



def exec2():
    button2.flash()

def exec3():
    button3.flash()
#------------------------------Les Fonctions------------------------------#


button1.configure(command=exec1)
button2.configure(command=exec2)
button3.configure(command=exec3)


#------------------------------Empaquetage------------------------------#
#input1.pack()
texte2.pack()
input2.pack()
button1.pack(pady=3)
texte1.pack()
#texte3.pack()
#input3.pack()
#button2.pack()
#button3.pack()
#------------------------------Empaquetage------------------------------#


root.mainloop()