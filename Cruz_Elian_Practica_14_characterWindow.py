import tkinter as tk
from PIL import ImageTk, Image
import json, requests

import urllib.parse, io

import Cruz_Elian_Practica_14_mainWindow
import Cruz_Elian_Practica_14_styles as st


Theme = {
    "primary": "#323232",
    "navbar": "#212121",
    "secondary": "#665c84",
    "accent": "#8ecccc",
    "text": "#fff"
}


def createWidgets(canvas, characterData):
    '''url = characterData['image']
    response = requests.get(url, stream=True)
    with open(''+characterData['name']+'.jpg', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)'''

    images = []

    raw_data = urllib.request.urlopen(characterData['image']).read()
    im = Image.open(io.BytesIO(raw_data)).resize((100,100))
    image = ImageTk.PhotoImage(im)
    label1 = tk.Label(canvas, image=image)
    label1.img = image
    label1.place(x=100, y=50)

    # append to list in order to keep the reference
    images.append(image)


    #edit = ImageTk.PhotoImage(Image.open("src/icons/"+characterData['name']+".jpg").resize((30,30)))
    #labelEdit = tk.Button(image=edit, bg=st.Theme["navbar"], highlightthickness = 0, bd = 0)
    #labelEdit.img = edit  #IMPORTANT LINE, Why? I HAVE NO CLUE
    #labelEdit.place(x=300, y=550)

    name = canvas.create_text(180, 170, text='Name: '+characterData['name'], fill=Theme['text'],  font=('Segoe UI', 12, 'normal'), width=280)

    height = canvas.create_text(180, 190, text='Height: '+str(characterData['height']), fill=Theme['text'],  font=('Segoe UI', 12, 'normal'), width=280)

    homeworld = canvas.create_text(180, 210, text='Homeworld: '+characterData['homeworld'], fill=Theme['text'],  font=('Segoe UI', 12, 'normal'), width=280)

    species = canvas.create_text(180, 230, text='Specie: '+characterData['species'], fill=Theme['text'],  font=('Segoe UI', 12, 'normal'), width=280)

    if 'affiliations' in characterData:
        affiliationsString = ''
        counter=0
        for affiliation in characterData['affiliations']:
            if counter>4:
                break
            affiliationsString+=affiliation+'\n'
            counter+=1
        affiliations = canvas.create_text(180, 360, text='Affiliations: \n'+affiliationsString,fill=Theme['text'],  font=('Segoe UI', 12, 'normal'), width=280)
    if 'masters' in characterData:
        mastersString = ''
        counter=0
        for master in characterData['masters']:
            if counter>4:
                break
            mastersString+=master+'\n'
            counter+=1

        masters = canvas.create_text(180, 500, text='Maters: \n'+mastersString, fill=Theme['text'], font=('Segoe UI', 12, 'normal'), width=280)
