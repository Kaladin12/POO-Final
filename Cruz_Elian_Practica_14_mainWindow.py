import tkinter as tk
import Cruz_Elian_Practica_14_styles as st
from PIL import ImageTk, Image
from Cruz_Elian_Practica_14_characterTemplate import *


mainRoot = None
mainCanvas = None

def showCharacters(characters, canvas):
    if (characters):
        height=90
        count=0
        if (isinstance(characters, list)):
            for character in characters:
                if count>6:
                    break
                characterTemplate(canvas, height, character)
                height += 75
                count+=1
    else:
        add = ImageTk.PhotoImage(Image.open("src/icons/add.png").resize((100,100)))
        label = tk.Button(master=canvas, image=add, bg=st.Theme["primary"], highlightthickness = 0, bd = 0) #,command=lambda: onAddEvent(root, students))
        label.img = add  #IMPORTANT LINE, Why? I HAVE NO CLUE jajaj
        label.place(relx=0.35, rely=0.3)
        tk.Label(master=canvas, text="Empty File. Add a Folder with +", font=('Segoe UI', 14, 'normal'), bg=st.Theme["primary"]).place(relx=0.08, rely=0.5)

def initCanvasAgain():
    print('called')
    global mainRoot, mainCanvas
    canvas = tk.Canvas( master=mainRoot,
        bd = 3,
        bg = 'blue',
        height = 300,
        width = 300
    )
    mainCanvas=canvas
    canvas.__init__(mainRoot,
        bg = st.Theme["primary"],
        height = 300,
        width = 300,
        bd=0,
        highlightthickness = 0
    )
    canvas.place(anchor=tk.NW, relwidth=1, relheight=1)
    
    return mainCanvas

def charactersComponent(root, characters):
    global mainRoot, mainCanvas
    mainRoot=root
    canvas = tk.Canvas( master=root,
        bd = 3,
        bg = 'blue',
        height = 300,
        width = 300
    )
    mainCanvas=canvas
    canvas.__init__(root,
        bg = st.Theme["primary"],
        height = 300,
        width = 300,
        bd=0,
        highlightthickness = 0
    )

    canvas.place(anchor=tk.NW, relwidth=1, relheight=1)
    navbar = canvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["navbar"])

    navTitle = tk.Label(master=canvas, text="Characters", fg=st.Theme["text"], bg=st.Theme["navbar"], font=('Segoe UI', 14, 'bold'))
    navTitle.place(anchor=tk.NW, x=10, y=15)
    showCharacters(characters, canvas)