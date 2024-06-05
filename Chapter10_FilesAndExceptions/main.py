from pathlib import Path

base_path = Path(r"C:\Users\Madhav\Desktop\Python Developer Course\Section13_File__IO\PCC_Ch10_Files")

def process_pi_file(filename):
    path = base_path / filename
    contents = path.read_text().strip()

    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            print()
            print(line)
            print()
            print(lines)
            print()

process_pi_file("learning_python.txt") 
