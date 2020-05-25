import json
import requests
import random


class characterMgr:
    def __init__(self, path, apiRoot):
        self.path = path
        self.apiRoot = apiRoot
    
    def getAllCharacters(self):
        try:
            res = requests.get(self.apiRoot)
            resDict = json.loads(res.content)
            with open(self.path, 'w') as file:
                json.dump(resDict, file)
            
            return resDict
        except: return None
    
    def findCharacter(self, name):
        with open(self.path) as file:
            data = json.load(file)
            for character in data:
                if character["name"] == name:
                    print('found!')
                    return character

    
