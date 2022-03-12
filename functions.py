# this file is for the irrelevant functions, so that main.py can be readable.
"""
Current updates to be done (sorted in order of importance):
NEED TO CREATE A STORYLINE.
Need to see what should be done for new players.
Can only save one game file for now, need to be able to save multiple files.
Create a function to load game data.
Game data could probably be in JSON, not sure yet. (i've successfully implemeted JSON now, need to make some finishing touches)
Create a tutorial for the game.
"""
import os
from datetime import datetime
import time
import game
import json

saveGameMetaData = { "title": "", "epochTime": 0 } # template: title, epochTime
saveGameData = {
    "coins": 0,
    "animals": {
        "rabbit": 0,
        "giraffe": 0,
        "skunk": 0,
        "deer": 0,
        "boar": 0
    },
    "exp": 0
}

def introScene():
    os.system("cls")
    print("(Enter any key to continue the dialog.)")
    print("Once upon a time the Gods reigned supreme. The people were afraid of them, they felt their existence and worshipped them.")
    input()
    print("But now, times have changed. The Gods have slackened and as a result people have started to become infidels.")
    input()
    print("You might be wondering what you are doing here; your confusion is valid.")
    input()
    print("You were once a mortal, but you proved yourself to be wild yet elegant, bold yet noble, fierce yet kind.")
    input()
    print("I will not reveal my identity to you, but I will tell you your objective:")
    input()
    print("It is up to you now to restore the status of the Gods. You may be a mortal but you will be able to accomplish this task. Go, human.")
    input()

def start():
    loader()
    os.system("cls")
    print("Welcome to God Simulator!")
    choice = input("Press 1 to load a previously saved game or press 2 to start a new game! Enter anything else if you want to exit!\n")
    if (choice != "1" and choice != "2"):
        print("Bye bye!")
        exit()
    elif (int(choice) == 1):
        if saveGameMetaData["epochTime"]:
            os.system("cls")
            date = datetime.fromtimestamp(saveGameMetaData["epochTime"]).strftime('%d/%m/%Y')
            time = datetime.fromtimestamp(saveGameMetaData["epochTime"]).strftime('%H:%M:%S')
            print(f"Title: " + {saveGameMetaData["title"]} + "\nSave date: {date}\nSave time: {time}")
            print("(Date format is dd/mm/yyyy, time format is hour/minute/second. Local time is shown.)")
            loader()
            input("\nThe game has loaded. Enter any key to continue...\n")
            game.menu()
        else:
            print("You don't have any save game!")
            input("Enter any key to continue...\n")
            choice = 2
    if (int(choice) == 2):
        os.system("cls")
        print("Hey there! This is a game about training to become the best God in the Universe!")
        print("You will have to fight enemies, powerful bosses and level up to become a true God.")
        input("Ready to start? Enter any key to continue...\n")
        introScene()
        game.menu()

# to save the game
def saver(data = None):
    os.system("cls")
    response = input("Beware! Saving will overwrite your current save file! Do you want to proceed? Enter yes or no: ").lower() if saveGameMetaData["epochTime"] else input("Do you want to save? Enter yes or no: ").lower()
    while response not in {"yes", "no"}:
        response = input("Please enter yes or no: ").lower()
    if response == "yes":
        saveGameMetaData["title"] = input("Enter the title for your save: ")
        saveGameMetaData["epochTime"] = int(time.time())
        # writing meta data
        file = open("metaData.json", "w")
        file.write(json.dumps(saveGameMetaData, indent = 4))
        file.close()
        # writing game data
        file = open("data.json", "w")
        file.write(json.dumps(saveGameData, indent = 4))
        file.close()
# to load the game
def loader():
    # loading meta data
    file = open("metaData.json", "r")
    saveGameMetaData = json.load(file)
    file.close()
    # loading game data
    file = open("data.json", "r")
    saveGameData = json.load(file)
    file.close()
# empty line at the end for no particular reason ¯\_(ツ)_/¯