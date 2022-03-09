# this file is for the irrelevant functions, so that main.py can be readable.
"""
Current updates to be done:
NEED TO CREATE A STORYLINE.
Need to see what should be done for new players.
Create a function to load game data.
Game data could probably be in JSON, not sure yet.
Create a tutorial for the game.
"""
import os
from datetime import datetime
from dateutil import tz

saveGameMetaData = [["sample 1", 1], ["sample 2", 2]] # template: title, saveTimeInEpoch
saveGameData = [] # template: stuff

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
    os.system("cls")

def start():
    print("Welcome to God Simulator!")
    choice = int(input("Press 1 to load a previously saved game or press 2 to start a new game! Enter anything else if you want to exit!\n"))
    if (choice != 1 and choice != 2):
        print("Bye bye!")
        exit()
    elif (choice == 1):
        if len(saveGameMetaData):
            os.system("cls")
            print("Which save game do you want to load?")
            for x in saveGameMetaData:
                date = datetime.fromtimestamp(x[1]).strftime('%d-%m-%Y')
                time = datetime.fromtimestamp(x[1]).strftime('%H:%M:%S')
                print(f"Title: {x[0]}\nSave date: {date}\nSave time: {time}\n")
            print("(Date format is dd/mm/yyyy and time format is hour/minute/second. Time is in UTC.)")
            userInput = input("Enter the title of your save game to load it: ")
            return userInput
        else:
            print("You don't have any save game!")
            input("Enter any key to continue...\n")
            choice = 2
            os.system("cls")
    if (choice == 2):
        print("Hey there! This is a game about training to become the best god in the Universe!")
        print("You will have to fight enemies, powerful bosses and level up to become a true God.")
        input("Ready to start? Enter any key to continue.\n")
        introScene()