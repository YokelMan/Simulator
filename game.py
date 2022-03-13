# a file consisting of all game related functions

import functions
import time
import os
import random
import requests

# dictionary of animals which can be hunted
animals = {
    0: "rabbit",
    1: "giraffe", # not realistic ik
    2: "skunk",
    3: "deer",
    4: "boar"
}
# values of the animals in the market, for now default value is 10 (idk in what currency)
animalValues = {
    "rabbit": 10,
    "giraffe": 10,
    "skunk": 10,
    "deer": 10,
    "boar": 10
}

def menu():
    while True:
        os.system("cls")
        try:
            print("Game menu:")
            print("1. Hunt")
            print("2. Train")
            print("3. Save")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            while choice not in {1, 2, 3, 4}:
                choice = int(input("Please enter a valid choice: "))
            if choice == 1:
                hunt()
            elif choice == 2:
                print("Work in progress!")
            elif choice == 3:
                functions.saver()
            elif choice == 4:
                # if it's been 5 minutes since the last save
                if functions.saveGameMetaData["epochTime"] + 300 < int(time.time()) and functions.saveGameMetaData["epochTime"]:
                    um = input("It has been 5 minutes since you last saved. Enter 1 to save your game or enter any other key to exit: ")
                    if um == "1":
                        functions.saver()
                        print("Saved game successfully! ", end = "")
                elif not functions.saveGameMetaData["epochTime"]:
                    um = input("You have not created a save file yet! Do you want to create one? Enter yes or no: ").lower()
                    while um not in {"yes", "no"}:
                        um = input("Please enter yes or no: ").lower()
                    if um == "yes":
                        functions.saver()
                        print("Saved game successfully! ", end = "")
                print("The game will now exit.")
                exit()
        except ValueError:
            input("Please enter a valid choice. Enter any key to continue.\n")       

def hunt():
    exp = 0
    os.system("cls")
    print("You walk to the forest to hunt animals.\n")
    while True:
        time.sleep(3)
        animal = random.choice(list(animals.values()))
        vowel = "an" if animal[0] in {"a", "e", "i", "o", "u"} else "a" # i like extra details like a/an
        if random.randint(1, 10) in {1, 2, 3}:
            print(f"You have come across {vowel} {animal}!")
            word = requests.get("https://random-word-api.herokuapp.com/word").json()[0]
            userTime = time.time()
            userWord = input(f"Quick! Hunt it UNDER 10 SECONDS! To hunt, type the word '{word.upper()}': ").lower()
            print()
            userTime  = time.time() - userTime
            if userWord == word and userTime <= 10:
                print(f"Gotcha! You caught the {animal}! Good job!")
                exp += random.randint(50, 100)
                print(f"From hunting this {animal} you also got {exp} experience points!")
                functions.saveGameData["exp"] += exp
                functions.saveGameData["animals"][animal] += 1
            elif userWord == word:
                print(f"The {animal} ran away because you took too much time in typing the word!")
            else:
                print("You didn't type the word correctly! Unlucky you!")
        else:
            print("You searched for a few minutes but unfortunately did not find any animal.")
        response = input("Want to go hunting again? Enter yes or no: ").lower()
        while response not in {"yes", "no"}:
            response = input("Please enter yes or no only: ").lower()
        if response == "yes":
            print()
            continue
        else:
            input("\nYou walk back to your home, tired from the hunt. Enter any key to continue...\n")
            break