# File I/O - File Input/Output

# Japanese Translator Exercise

import sys

sys.path.append(
    r"C:\Users\Madhav\AppData\Local\Programs\Python\Python312\Lib\site-packages\translate\Translator"
)
# from translate import Translator

from translate import Translator

translator = Translator(to_lang="ja")

file = open("sad.txt")

translation = translator.translate(file)
print(translation)

"""

# write mode (mode="w") creates a new file if it doesn't already exist or overwrites and existing one
# text = my_file.write("hey its me!")
try:
    with open("sad.txt", mode="r") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO error")
    raise err

my_file = open("test.txt")

print(my_file.readlines())
my_file.close()


print(
    my_file
)  # prints "<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>"

print(my_file.read())  # reads test.txt file | prints "hi my name is Madhav"
my_file.seek(0)
print(my_file.read())  # reads test.txt file | prints "hi my name is Madhav"
my_file.seek(0)
print(my_file.read())  # reads test.txt file | prints "hi my name is Madhav"
my_file.seek(0)

print(my_file.readline())
"""
