import json, requests

class usersManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.path = 'users.json'

    def userAuth(self):
        with open(self.path) as file:
            users = json.load(file)
            for user in users:
                print(user, user["username"] == self.username, user["password"] == self.password)
                if user["username"] == self.username:
                    if user["password"] == self.password:
                        print('found!')
                        return user

    def signUpUser(self):
        with open('users.json') as file:
            users = json.load(file)
        template = {
            "username":self.username,
            "password":self.password,
            "settings":[],
            "favourites":[]
        }
        users.append(template)
        with open('users.json', 'w', newline='\n') as file:
            json.dump(users, file, indent=4)