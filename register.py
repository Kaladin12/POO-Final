import json, requests
import tkinter as tk
from PIL import ImageTk, Image


from userManager import *
import login

Theme = {
    "primary": "#323232",
    "navbar": "#212121",
    "secondary": "#665c84",
    "accent": "#8ecccc",
    "text": "#fff"
}

class signUp:
    def __init__(self, root):
        self.root=root
        self.showRegisterWidgets()
    
    def registerClick(self, username, password):
        uMgr = usersManager(username.get(), password.get())
        responseAuth = uMgr.signUpUser()
        login.login(self.root)

    def showRegisterWidgets(self):
        canvas = tk.Canvas(self.root, 
        height = 360,
        width = 640,
        bg = Theme["primary"])
        canvas.place(anchor=tk.NW, relwidth=1, relheight=1)
        navbar = canvas.create_rectangle(0, 0, 360, 50, fill=Theme["navbar"])

        navTitle = tk.Label(master=canvas, text="Sign Up", fg=Theme["text"], bg=Theme["navbar"], font=('Segoe UI', 14, 'bold'))
        navTitle.place(anchor=tk.NW, x=50, y=15)

        studentsTitle = tk.Label(master=canvas, text="Name", fg=Theme["text"], bg = Theme["primary"], font=('Segoe UI', 10, 'bold'))
        studentsTitle.place(anchor=tk.NW, x=10, y=70)

        nameInput = tk.Entry(master=canvas, bg=Theme["text"], fg="gray", highlightthickness = 0, bd=0, width=42)
        nameInput.place(x=11, y=110)
        nameInput.insert(0, "Username")
        
        passwordInput = tk.Entry(master=canvas, bg=Theme["text"], fg="gray", highlightthickness = 0, bd=0, width=42)
        passwordInput.place(x=11, y=220)
        passwordInput.insert(0, "Password")

        addBtn = tk.Button(bg=Theme["accent"], fg='white', width=38, text="Log In", command= lambda : self.registerClick(nameInput, passwordInput))
        addBtn.place(x=11, y=275)