from tkinter import *
root = Tk()
root.title('Screen printer')

cords=[]
buttons=[]
liste_detect=[]
compteur = 0


for i in range(5):
    for ii in range(5):
        liste_detect.append((i,ii))
        but=Button(root, text=f"({i},{ii})", bg='green', bd=5, relief='groove',width=2,height=2,padx=20,command=lambda x=[(i,ii),compteur]:cords_button(x))
        but.grid(column=i, row=ii)
        buttons.append(but)
        compteur += 1


def cords_button(c_button):
    comp = 0
    buttons[c_button[1]].configure(bg="grey")
    for i in range(len(cords)): # sert à éviter les duplications dans cords
        if cords[i] == c_button[0]:
            comp = 1
    if comp == 0:
        cords.append(c_button[0])

def clear_cords():
    global buttons
    for i in range(len(buttons)):
        buttons[i].configure(bg="green")

    global cords
    cords=[]
    print("Cleared !")

def compileur():
    global cords, buttons
    for i in range(len(buttons)):
        buttons[i].configure(bg="green")
    print(f"{returner(*cords)}\ndisplay.show(Image(\"{returner(*cords)}\"))")
    cords=[]

def returner(*args):
    """
    convertit un nombre de tuples allant de 0 à 25 en coordonnés syntaxisés
    """
    liste=[[str(0) for _ in range(5)] for _ in range(5)]
    for (x,y) in args:
        liste[y][x]= str(scale.get())
    return ":".join(list(map(lambda x: "".join(x),liste)))


value = StringVar()
scale = Scale(root,orient="horizontal", from_=1,to=9,label="LUM",length=80,variable=value)
compil=Button(root, text="CMPL", bg="purple",width=2,height=2,padx=20,command=compileur)
clear=Button(root, text="CLR", bg="red",width=2,height=2,padx=20,command=clear_cords)
scale.grid(column=0,row=5)
compil.grid(column=2,row=5)
clear.grid(column=3,row=5)

    
if __name__=='__main__':
    root.mainloop()

