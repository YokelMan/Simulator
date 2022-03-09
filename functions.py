# this file is for the irrelevant functions, so that main.py can be readable.
"""
Current updates to be done (sorted in order of importance):
NEED TO CREATE A STORYLINE.
Need to see what should be done for new players.
Can only save one game file for now, need to be able to save multiple files.
Create a function to load game data.
Game data could probably be in JSON, not sure yet.
Create a tutorial for the game.
"""
import os
from datetime import datetime

saveGameMetaData = ["sample 1", 1] # template: title, saveTimeInEpoch
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
            date = datetime.fromtimestamp(saveGameMetaData[1]).strftime('%d-%m-%Y')
            time = datetime.fromtimestamp(saveGameMetaData[1]).strftime('%H:%M:%S')
            print(f"Title: {saveGameMetaData[0]}\nSave date: {date}\nSave time: {time}\n")
            loader()
            input("\nThe game has loaded. Enter any key to continue...\n")
            pass # <- some function to start the game
        else:
            print("You don't have any save game!")
            input("Enter any key to continue...\n")
            choice = 2
            os.system("cls")
    if (choice == 2):
        print("Hey there! This is a game about training to become the best God in the Universe!")
        print("You will have to fight enemies, powerful bosses and level up to become a true God.")
        input("Ready to start? Enter any key to continue...\n")
        introScene()
        pass # <- some function to start the game

# to save the game
def saver(data = None):
    response = input("Beware! Saving will overwrite your current save file! Do you want to proceed? Enter Yes or No: ").lower()
    while response not in {"yes", "no"}:
        response = input("Please enter yes or no: ").lower()
    saveGameMetaData[0] = input("Enter the title for your save: ")
    time = datetime.now()
    timeArr = [time.strftime("%Y"), time.strftime("%m"), time.strftime("%d"), time.strftime("%H"), time.strftime("%M"), time.strftime("%S")]
    epochTime = int(datetime(int(timeArr[0]), int(timeArr[1]), int(timeArr[2]), int(timeArr[3]), int(timeArr[4]), int(timeArr[5])).timestamp())
    saveGameMetaData[1] = epochTime

# to load the game
def loader():
    pass