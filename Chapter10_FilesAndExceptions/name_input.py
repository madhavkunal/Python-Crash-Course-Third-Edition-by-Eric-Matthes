from pathlib import Path

while True:
    contents = input("Please enter your name (or type 'quit' to exit): ")
    if contents.lower() == "quit":
        break  # Exit the loop if the user enters 'quit'

    path = Path("guest_book.txt")
    with open(path, "a") as file:  # Use 'a' mode for appending
        file.write(contents + "\n")  # Add a newline for each entry

print("Exiting the guest book program.")
