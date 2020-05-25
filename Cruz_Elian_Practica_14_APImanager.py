import json
import requests

class apiMgr:
    def __init__(self, path, apiRoot):
        self.path = path
        self.apiRoot = apiRoot
    
    def getAllCharacters(self):
        try:
            res = requests.get(self.apiRoot).text
            print('res', res)
            resDict = json.loads(res)
            print(resDict)
            with open(self.path, 'wb') as file:
                json.dump(resDict, file)
            
            return resDict
        except: return None
