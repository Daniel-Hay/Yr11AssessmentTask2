from tkinter import *
import json
import requests

print("hello")
response = requests.get("https://nba-stats-db.herokuapp.com/api/playerdata/name/Nikola Jokić") 
print(response.status_code)
print(response.json())

root = Tk()  # create a root widget
root.title("Tk Example")
root.configure(background="green4")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("300x300+800+300")  # width x height + x + y
root.mainloop()

