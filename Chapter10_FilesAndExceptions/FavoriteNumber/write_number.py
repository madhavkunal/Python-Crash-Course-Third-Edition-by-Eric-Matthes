# Exercise 10-11 (Favorite Number)

from pathlib import Path
import json

path = Path('favorite_numbers.json')    # global variable

def write_number():
    favorite_number = input("Please enter your favorite number: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
write_number()