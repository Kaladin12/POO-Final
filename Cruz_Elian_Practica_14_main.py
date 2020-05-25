import tkinter as tk
from PIL import ImageTk, Image
from Cruz_Elian_Practica_14_mainWindow import *
from Cruz_Elian_Practica_14_characterMgr import *
from login import *

screenSize = { 'width': 360, 'height': 640 }

root = tk.Tk()
root.title('API')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)

path = 'data.json'
API = 'https://cdn.rawgit.com/akabab/starwars-api/0.2.1/api/all.json'

mgr = characterMgr(path, API)

characters = mgr.getAllCharacters()
#print(characters)

newLogin = login(root)
#charactersComponent(root, characters)


root.mainloop()