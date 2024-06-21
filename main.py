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
        players_data = json.loads(response.text)
        for x in range(0, 7):
            random_number = random.randrange(51)
            random_player = players_data["results"][random_number]["player_name"]
            player = nbaData(random_player)
            player.retrieveStats()
            x += 1

class nbaData(API):
    def __init__(self, name):
        self.stats = f"https://nba-stats-db.herokuapp.com/api/playerdata/name/{name}"

    def retrieveStats(self):
        player_response = requests.get(self.stats)
        print(player_response.status_code)
        player_data = json.loads(player_response.text)
        print(player_data)
        

class main:
    def choice1():
        print("hello")
        nba_API = API("https://nba-stats-db.herokuapp.com/api/playerdata/season/2023")
        nba_API.openData()

    def choice2():
        print("yo")
        nba_API = API("https://nba-stats-db.herokuapp.com/api/playerdata/season/2017")
        nba_API.openData()

# Make the user choose which year they want to play


def choice():
    # Use tkinter to show choices
    button1 = ctk.CTkButton(app, text="2023", command=main.choice1)
    button1.pack()
    button2 = ctk.CTkButton(app, text="2017", command=main.choice2)
    button2.pack()

if __name__ == '__main__':
    choice()
    #main.choice1()
    #main.choice2()
    app.mainloop()