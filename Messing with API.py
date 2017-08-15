#Messing around with API
import requests
#this program should show give champ info based on id input

#function to provide json file
def championinfo(cID, uAPIkey):
    info = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champions/"+ cID +"/?api_key="+uAPIkey)
    return info.json()
#function to check if the champ is free to play based on the chamions id
def f2p(info):
    print [info][0]['freeToPlay']
#required inputs for program to run    
cID = (str)(raw_input("enter a champ id number"))
uAPIkey =(str) (raw_input ("enter your api key"))
print championinfo(cID, uAPIkey)
info = championinfo(cID, uAPIkey)
f2p(info)
