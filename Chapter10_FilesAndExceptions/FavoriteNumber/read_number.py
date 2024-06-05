# Exercise 10-11 (Favorite Number)


from pathlib import Path
import json

path = Path('favorite_numbers.json')    # global variable


def read_number():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number} !")
read_number()