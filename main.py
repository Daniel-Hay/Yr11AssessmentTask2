from tkinter import *
import json
import requests
import customtkinter as ctk
from random import choice
import random

app = ctk.CTk()
app.geometry("600x500")
app.title("NBA Trivia Game")

## Use comments and docstrings




class API:    
    def __init__(self, url):
        self.url = url
    
    def openData(self):
        response = requests.get(self.url)
        print(response.status_code)
        self.parseData(response)

    def parseData(self, response):
        # Change from global after testing to more sophisticated method





        global playersData
        playersData = json.loads(response.text)
        for x in range(0, 7):
            # Change from global after testing to more sophisticated method
            global randomNumber
            randomNumber = random.randrange(51)
            randomPlayer = playersData["results"][randomNumber]["player_name"]
            print(randomPlayer)
            player = nbaData(randomPlayer)
            player.retrieveStat()
            x += 1

class nbaData(API):
    def __init__(self, name):
        self.statsList = ["PTS", "AST", "TRB", "STL", "BLK", "TOV", "PF"]
        self.name = name

    def randomStat(self):
        randomStat = random.choice(self.statsList)
        print(randomStat)
        return randomStat

    def retrieveStat(self):
        randomPlayerStat = playersData["results"][randomNumber][self.randomStat()]
        playerGamesPlayed = playersData["results"][randomNumber]["games"]
        randomPlayerStat = round(randomPlayerStat / playerGamesPlayed, 2)
        print(randomPlayerStat)
        
        
# Make the user choose which year they want to play

def choice(choice):
    chosenYear = choice
    print(chosenYear)
    print("optionmenu dropdown clicked:", choice)

combobox = ctk.CTkOptionMenu(master=app, values=["2023", "2017"], command=choice)
combobox.pack(padx=20, pady=10)
combobox.set("2023")  # sets initial value

def start():
    print("button pressed")
    nba_API = API(f"https://nba-stats-db.herokuapp.com/api/playerdata/season/{combobox.get()}")
    nba_API.openData()

startButton = ctk.CTkButton(app, text="Start Game", command=start)
startButton.pack(pady=10)

if __name__ == '__main__':
    app.mainloop()