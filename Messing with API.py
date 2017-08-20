#Messing around with API
import requests
import sys
#this program should show give champ info based on id input

#function to provide json file
def champinfo(cID, uAPIkey):
    info = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champions/"+ cID +"/?api_key="+uAPIkey)
    return info.json()
#function to check if the champ is free to play based on the chamions id
free = (str)
def f2p(info):
    print [info][0]['freeToPlay']
#required inputs for program to run    
cID = (str)(raw_input("enter a champ id number"))
uAPIkey =(str) (raw_input ("enter your api key"))

#Below I make a while statement that makes the program more user friendly incase it ever expands into somthing useful and distributable as opposed to just an excercise
#I also had some time to kill
while True:
    func = (str)(raw_input("what would you like me to do? (type help for commands)"))
    if func == "champinfo":
        print champinfo(cID, uAPIkey)
    elif func == "f2p":
        info = champinfo(cID, uAPIkey)
        f2p(info)
    elif func == "help":
        print "type"
        print "champinfo for champion informations"
        print "f2p to find out if the champion is free to play"
        print "exit to exit"
    elif func == "exit":
        break
    else:
        print "enter a valid command"

sys.exit()
