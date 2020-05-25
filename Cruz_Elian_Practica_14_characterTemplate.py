#this creates a template for every canvas shown on mainWindow component
import tkinter as tk
from PIL import ImageTk, Image
import Cruz_Elian_Practica_14_styles as st
from Cruz_Elian_Practica_14_characterMgr import *
import Cruz_Elian_Practica_14_mainWindow
from Cruz_Elian_Practica_14_styles import *
from Cruz_Elian_Practica_14_characterMgr import *
from Cruz_Elian_Practica_14_characterWindow import *

class characterTemplate:
    def __init__(self, mainCanvas, relativeHeight, character):
        self.canvas = tk.Canvas() #created as canvas inside main canvas
        self.character=character
        canvas = tk.Canvas( master=mainCanvas, 
        bd = 3,
        bg = 'white',
        height = 75,
        width = 360
        )

        canvas.__init__(mainCanvas,
            bg = st.Theme["primary"],
            height = 75,
            width = 360,
        )

        canvas.place(anchor=tk.NW, x=-1, y=relativeHeight)  #places new canvas
        canvas.bind("<Button-1>", lambda myCharacter=self.character:self.click(myCharacter))#this fetches a click event to each character canvas

        self.showCharacterData(self.character, canvas)

    def showCharacterData(self, character, canvas):

        raw_data = urllib.request.urlopen(character['image']).read()
        im = Image.open(io.BytesIO(raw_data)).resize((30,30))
        image = ImageTk.PhotoImage(im)
        label1 = tk.Label(canvas, image=image)
        label1.img = image
        label1.place(relx=0.0, rely=0.3)

        nombre = tk.Label(master=canvas, text=character['name'], fg=Theme["text"], bg=Theme["primary"], font=('Segoe UI', 12, 'normal'))
        nombre.place(relx=0.5, rely=0.3)
    
    def goBack(self, root):
        mgr = characterMgr('data.json', 'https://cdn.rawgit.com/akabab/starwars-api/0.2.1/api/all.json')
        characters = mgr.getAllCharacters()
        Cruz_Elian_Practica_14_mainWindow.charactersComponent(root, characters)

    def click(self, myCharacter):
        newCanvas = Cruz_Elian_Practica_14_mainWindow.initCanvasAgain() 

        navbar = newCanvas.create_rectangle(0, 0, 360, 50, fill=st.Theme["navbar"])

        back = ImageTk.PhotoImage(Image.open("src/icons/back.png").resize((30,30)))
        label = tk.Button(image=back, bg=st.Theme["navbar"], highlightthickness = 0, bd = 0, command=lambda: self.goBack(Cruz_Elian_Practica_14_mainWindow.mainRoot))
        label.img = back  #IMPORTANT LINE, Why? I HAVE NO CLUE
        label.place(x=10, y=10)

        navTitle = tk.Label(master=newCanvas, text="Character Info", fg=st.Theme["text"], bg=st.Theme["navbar"], font=('Segoe UI', 14, 'bold'))
        navTitle.place(anchor=tk.NW, x=50, y=15)

        character = characterMgr('data.json', 'http://intergalacticdb.me/api/characters/').findCharacter(self.character["name"])
        createWidgets(newCanvas, character)

        print(character)

