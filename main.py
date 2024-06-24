# Imports all required modules

from tkinter import *
import json
import requests
import customtkinter as ctk
from random import choice
import random
import os
import sys
from abc import ABC, abstractmethod

# Creates the main window
app = ctk.CTk()
app.geometry("600x500")
app.title("NBA Trivia Game")
ctk.set_appearance_mode("Dark") 


## Use comments and docstrings

class API:
    """
    A class representing an API.
    
    Attributes:
        url (str): The URL of the API.
        
    Methods:
    openData: Gets the data from the API and converts the json data into a readable python dictionary
    retrieveStat: Parent method of the child class nbaData, demonstrating abstraction
    """
    def __init__(self, url):
        self.url = urlstring
        
    def openData(self):
        response = requests.get(self.url)
        playersData = json.loads(response.text)
        return playersData
    
    @abstractmethod
    def retrieveStat(self):
        pass

# Class that retrieves the data from the API, randomly selecting the player and their related stat
class nbaData(API):
    """
    A class representing NBA player data.
    
    Attributes:
        url (str): The URL of the API.
        
    Methods:
        retrieveStat: Retrieves a random player and their related stat.
    """
    def __init__(self, url):
        super().__init__(url)

    def retrieveStat(self):
        randomPlayerID = random.randrange(100)
        apiData = API(self.url)
        callRandomData = apiData.openData()
        randomStat = random.choice(["PTS", "AST", "TRB", "STL", "BLK", "TOV", "PF"])
        randomPlayer = callRandomData["results"][randomPlayerID]["player_name"]
        randomPlayerStat = callRandomData["results"][randomPlayerID][randomStat]
        playerGamesPlayed = callRandomData["results"][randomPlayerID]["games"]
        randomPlayerStat = round(randomPlayerStat / playerGamesPlayed, 2)
        return randomPlayer, randomPlayerStat, randomStat

# Class that creates questions based on NBA data
class QuestionSet:
    """
    A class representing a set of questions based on NBA data.

    Attributes:
    nba_data (dict): A dictionary containing NBA player data.
    questions (list): A list of questions.

    Methods:
    create_player_questions: Creates a question based on a player's name and stat.
    create_questions: Creates questions based on the NBA data.
    get_questions: Returns the list of questions.
    """    
    def __init__(self, nba_data):
        self.nba_data = nba_data
        self.questions = []

    def create_player_questions(self, player_name, player_stat):
        question = f"What was the average {player_stat}s of {player_name} in {combobox.get()}?"
        self.questions.append(question)

    def create_questions(self):
        for player in self.nba_data:
            question = f"What is the {self.nba_data[player]['stat']} of {player}?"
            self.questions.append(question)

    def get_questions(self):
        return self.questions

class Question:
    """
    A class representing a question and its answer.
    
    Attributes:
        _question (str): The question.
        _answer (str): The answer to the question.
    """
    
    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    def __str__(self):
        return self._question

class User:
    """
    A class representing a user.

    Attributes:
        _score (int): The user's score.

    Methods:
        increase_score: Increases the user's score by 1.
    """
    
    def __init__(self):
        self._score = 0

    def increase_score(self):
        self._score += 1

# Header of the App
header = ctk.CTkLabel(app, text="Nba Trivia", fg_color="transparent", font=("Playwrite US Modern", 50))
header.pack(pady=10)

# Question asking the user which year they want to play
select_question = ctk.CTkLabel(app, text="Which year do you want to play?", fg_color="transparent", font=("Playwrite US Modern", 25))
select_question.pack(pady=10)
        
# Make the user choose which year they want to play
combobox = ctk.CTkOptionMenu(master=app, values=["2023", "2022", "2021", "2020", "2019", "2018", "2017"])
combobox.pack(padx=20, pady=20)
combobox.set("2023")  # sets initial value

# Calls the API with the selected year from above
def start():
    # Clears the app from previous widgets
    header.pack_forget()
    select_question.pack_forget()
    combobox.pack_forget()
    startButton.pack_forget()
    questionTkinter()

startButton = ctk.CTkButton(app, text="Start Game", command=start)
startButton.pack(pady=10)

# Creates instances of both users
user1 = User()
user2 = User()

def questionTkinter():
    """
    This function generates a question using NBA player statistics and displays it in a Tkinter GUI.
    It allows two players to enter their answers, checks the answers, updates the scores, and determines the winner.
    The function also provides a button to move to the next question.
    """

    # Generate the questions

    # Clear all widgets
    for widget in app.winfo_children():
        widget.pack_forget()

    def submit():
        # Clears the app from previous widgets
        questiondisplay.pack_forget()
        actualquestion.pack_forget()
        entry.pack_forget()
        submit.pack_forget()
        entry2.pack_forget()

        # Checks Answer
        answer = ctk.CTkLabel(app, text="Answer: " + str(player_stat), fg_color="transparent")
        answer.pack(pady=10)

        p1_answer = ctk.CTkLabel(app, text="Player 1 Answer: " + entry.get(), fg_color="transparent")
        p1_answer.pack(pady=10)

        p2_answer = ctk.CTkLabel(app, text="Player 2 Answer: " + entry2.get(), fg_color="transparent")
        p2_answer.pack(pady=10)

        def check_answer(player_stat):
            # Checks if the user input is a number, if not, it will display an error message
            try:

                def winner(Player):
                    answer.pack_forget()
                    p1_answer.pack_forget()
                    p2_answer.pack_forget()
                    score_label.pack_forget()

                    winner_label = ctk.CTkLabel(app, text=f"{Player} Wins!", fg_color="green", font=("Playwrite US Modern", 50))
                    winner_label.pack(pady=10)


                player_stat = float(player_stat)
                user1_answer = float(entry.get())
                user2_answer = float(entry2.get())

                user1_difference = abs(user1_answer - player_stat)
                user2_difference = abs(user2_answer - player_stat)

                # Checks which user's answer is closer to the actual answer
                if user1_difference < user2_difference:
                    user1.increase_score()
                elif user2_difference < user1_difference:
                    user2.increase_score()
                
                # Updates the user's scores
                score_label = ctk.CTkLabel(app, text=f"Score: Player 1: {user1._score}, Player 2: {user2._score}", fg_color="transparent")
                score_label.pack(pady=10)

                # Checks if a user has won by reaching 7 points
                if user1._score == 7:
                    winner("Player 1")

                elif user2._score == 7:
                    winner("Player 2")

                next_question_button = ctk.CTkButton(app, text="Next Question", command=questionTkinter)
                next_question_button.pack(pady=10)

            except ValueError:
                # If player inputs a string, it will display an error message and move to the next question
                error_label = ctk.CTkLabel(app, text="Please enter a number", fg_color="red")
                error_label.pack(pady=10)
                next_question_button = ctk.CTkButton(app, text="Next Question", command=questionTkinter)
                next_question_button.pack(pady=10)

        check_answer(player_stat)

    global urlstring
    urlstring = f"https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/total/season/{combobox.get()}"
    nba_API = API(urlstring)

    # Creates an instance of nbaData
    nba_data = nbaData(nba_API)

    # Creates an instance of QuestionSet
    question_set = QuestionSet(nba_data.retrieveStat())

    player_name, player_stat, random_stat = nba_data.retrieveStat()
    question_set.create_player_questions(player_name, random_stat)

    questiondisplay = ctk.CTkLabel(app, text=f"Question 1", fg_color="transparent")
    questiondisplay.pack(pady=10)

    actualquestion = ctk.CTkLabel(app, text=question_set.get_questions()[0], fg_color="transparent")
    actualquestion.pack(pady=10)

    entry = ctk.CTkEntry(app, placeholder_text="Player 1 Answer")
    entry.pack(pady=10)

    entry2 = ctk.CTkEntry(app, placeholder_text="Player 2 Answer")
    entry2.pack(pady=10)

    submit = ctk.CTkButton(app, text="Submit", command=submit)
    submit.pack(pady=10)

# App loop created when program is ran
if __name__ == '__main__':
    app.mainloop()