import json, requests
import tkinter as tk
from PIL import ImageTk, Image

from userManager import *
from Cruz_Elian_Practica_14_characterMgr import *
from Cruz_Elian_Practica_14_mainWindow import *
from register import *

Theme = {
    "primary": "#323232",
    "navbar": "#212121",
    "secondary": "#665c84",
    "accent": "#8ecccc",
    "text": "#fff"
}

class login:
    def __init__(self, root):
        self.root=root

        self.showLoginWidgets()

    def logInClick(self, username, password):
        uMgr = usersManager(username.get(), password.get())
        responseAuth = uMgr.userAuth()
        print(responseAuth)
        if responseAuth:
            API = 'https://cdn.rawgit.com/akabab/starwars-api/0.2.1/api/all.json'
            mgr = characterMgr('data.json', API)
            characters = mgr.getAllCharacters()
            charactersComponent(self.root, characters)

    def registerClick(self):
        signUp(self.root)

    def showLoginWidgets(self):
        canvas = tk.Canvas(self.root, 
        height = 360,
        width = 640,
        bg = Theme["primary"])
        canvas.place(anchor=tk.NW, relwidth=1, relheight=1)
        navbar = canvas.create_rectangle(0, 0, 360, 50, fill=Theme["navbar"])

        navTitle = tk.Label(master=canvas, text="Log In", fg=Theme["text"], bg=Theme["navbar"], font=('Segoe UI', 14, 'bold'))
        navTitle.place(anchor=tk.NW, x=50, y=15)

        studentsTitle = tk.Label(master=canvas, text="Name", fg=Theme["text"], bg = Theme["primary"], font=('Segoe UI', 10, 'bold'))
        studentsTitle.place(anchor=tk.NW, x=10, y=70)

        nameInput = tk.Entry(master=canvas, bg=Theme["text"], fg="gray", highlightthickness = 0, bd=0, width=42)
        nameInput.place(x=11, y=110)
        nameInput.insert(0, "Username")
        
        passwordInput = tk.Entry(master=canvas, bg=Theme["text"], fg="gray", highlightthickness = 0, bd=0, width=42)
        passwordInput.place(x=11, y=220)
        passwordInput.insert(0, "Password")

        addBtn = tk.Button(bg=Theme["accent"], fg='white', width=38, text="Log In", command= lambda : self.logInClick(nameInput, passwordInput))
        addBtn.place(x=11, y=275)

        noRegistered = tk.Button(bg=Theme["accent"], fg='white', width=38, text="Click here if you don't have an account", command = self.registerClick)
        noRegistered.place(x=11, y=330)