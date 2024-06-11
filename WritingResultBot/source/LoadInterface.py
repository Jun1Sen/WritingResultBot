import json

def LoadInterface(sourceStrings):
    try:
        with open(sourceStrings, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {sourceStrings} not found. Error in LoadInterface() LangInterface.py")

