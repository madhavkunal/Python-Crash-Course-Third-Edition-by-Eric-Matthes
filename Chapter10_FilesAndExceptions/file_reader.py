from pathlib import Path

base_path = Path(r"C:\Users\Madhav\Desktop\Python Developer Course\Section13_File__IO\PCC_Ch10_Files")

def process_pi_file(filename):
    path = base_path/filename
    contents = path.read_text().strip()
    lines = contents.splitlines()
    pi_string = "".join(line.strip() for line in lines)
    print(pi_string)
    print(f"{pi_string[:15]}...")
    print(len(pi_string))

process_pi_file("pi_30_digits.txt")
process_pi_file("pi_500_digits.txt")

# path = Path(r"C:\Users\Madhav\Desktop\Python Developer Course\Section13_File__IO\PCC_Ch10_Files\pi_30_digits.txt")

# contents = path.read_text().strip()
# lines = contents.splitlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.strip()  # strip whitespace

# print(pi_string)
# print(len(pi_string))


# path = Path(r"C:\Users\Madhav\Desktop\Python Developer Course\Section13_File__IO\PCC_Ch10_Files\pi_500_digits.txt")

# contents = path.read_text().strip()
# lines = contents.splitlines()
# pi_string = ""
# for line in lines:
#    pi_string += line.strip()  # strip whitespace

# print(pi_string)
# print(len(pi_string))


# 1. import Path class from pathlib (path library)
# pathlib is a library (collection of modules with wide tooling and functionality) that makes it easier to work with files and directories and is cross OS for us and for users. libraries can be built-in to python root directory or imported from PyPI (Python Package Index) repositories
# 2. instantiate Path class as path object which points to pi_digits.txt file by passing in the absolute file path
# 3. read the filetext of the path object (pi_digits.txt file) and assign it to the contents variable and remove (strip) blank line and extra whitespace at end
# 4. print the contents (of the pi_digits.txt file)

# Relative file path tells python to look for a given location relative to the present working directory (pwd)
# Absolute file path tells python the exact file location in computer storage and starts at the system's root folder (always longer than relative file path)
