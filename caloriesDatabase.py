import json
import os


""" This is a simple JSON file that keeps a list of entries as dictionaries
so each entry: {"food":"...", "calories":"...", "meal":"..."} """


class CalorieDatabase:

    def __init__(self, filename="calories_data.json"):
        self.filename = filename
        #this will create a file if missing
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    #function that loads the data from the JSON file if it contains anything or not 
    def loadData(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                return []
        except Exception:
            #on any error, it returns empty list
            return []

    #the functions that saves the data in the json file
    def saveData(self, entries):
        try:
            with open(self.filename, "w") as f:
                json.dump(entries, f, indent=2)
        except Exception as e:
            print("Failed to save data:", e)