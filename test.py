import json, requests

with open('users.json') as file:
    users = json.load(file)
template = {
    "username":"otro",
       "password":"dekfn",
       "settings":[
 
       ],
       "favourites":[
 
       ]
}
users.append(template)

with open('users.json', 'w', newline='\n') as file:
    json.dump(users, file, indent=4)

