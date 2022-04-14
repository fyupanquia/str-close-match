import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        w = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean '%s' instead? [Y/N]: " % w)
        if yn == "Y":
            return data[w]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter a spanish word you wanna translate:")
print(translate(word))