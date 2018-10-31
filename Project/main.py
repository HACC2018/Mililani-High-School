import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("1.10.0")

from database.database import Database

#loads the code from database/database.py

class Application(App):

    def build(self):
    	return Label(text="Hello World")


    def LoadData(self):
    	pass

if __name__ == "__main__":
	Application().run() 