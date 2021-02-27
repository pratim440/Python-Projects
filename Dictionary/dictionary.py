import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean ' %s ' instead?" %get_close_matches(word, data.keys())[0])
        decide = input("press Y for yes or N for no:  ")
        if decide == "y" or decide == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n" or decide == "N":
            return("Pugger your paw steps on wrong keys.")
        else:
            return("You have entered wrong input please enter just  or n")
    else:
        print("Pugger your paw steps on wrong key.")



word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
