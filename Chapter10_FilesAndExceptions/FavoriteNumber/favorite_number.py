# Exercise 10-11 (Favorite Number Remembered)

from pathlib import Path
import json

path = Path('favorite_numbers.json')    # global variable

# favorite_number and contents are local variables

def write_number():
    favorite_number = input("Please enter your favorite number: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
write_number()


def read_number():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number} !")
read_number()