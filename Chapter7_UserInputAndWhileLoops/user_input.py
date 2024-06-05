# # Exercise 7-1 (Rental Car)

# rental_car = input("What kind of rental car would you like? ")
# rental_car = rental_car.title()
# print(f"Let me see if I can find you a {rental_car}")

# # Exercise 7-2 (Restaurant Seating)

# def word_to_num(word):
#     number_dict = {
#         'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
#         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
#         'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
#         'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20
#     }
#     word = word.lower()  # Convert the input to lowercase
#     if word in number_dict:
#         return number_dict[word]
#     else:
#         return None

# def string_to_int(input_str):
#     try:
#         # Try to convert the input string to an integer
#         number = int(input_str)
#         return number
#     except ValueError:
#         # If the conversion fails, it's not a valid number
#         return None

# group_size_input = input("How many are you? ")
# group_size = string_to_int(group_size_input)

# if group_size is None:
#     # If the input is not a valid number, try to convert it from alphabetical to numerical
#     group_size = word_to_num(group_size_input)

# if group_size is None:
#     print("Invalid input. Please enter a valid number.")
# elif 9 <= group_size <= 16:
#     print("Sorry, you will have to wait for a table.")
# elif group_size >= 17:
#     print("Sorry, we have a seating limit of 16 people.")
# else:
#     print("Your table is ready! Please follow me.")


# #Exercise 7-3 (Multiples of Ten)

# multiple = input("Give me a number >= 9! ")
# multiple = int(multiple)

# if multiple % 10 == 0:
#     print("The number is a multiple of 10!")
# else:
#     print("Sorry, your number is not a multiple of 10!")


# Exercise 7-4 (Pizza Toppings)

# print("\nPlease type 'Done' when you are finished adding toppings")

# toppings_list = []  # Create an empty list to store the toppings

# while True:
#     pizza_toppings = input("\nWhich pizza toppings would you like? ")
    
#     if pizza_toppings.lower() == 'done':
#         break
#     elif pizza_toppings == '':
#         print("Please enter a valid topping or type 'Done' to finish.")
#     else:
#         toppings_list.append(pizza_toppings.title())  # Add the topping to the list
#         print(f"\t{pizza_toppings.title()} added to your pizza!")

# # Print the list of toppings in a single line
# print("\n\tYour pizza will have the following toppings: " + ", ".join(toppings_list))
# print()



# Exercise 7-5 (Movie Tickets)

# print("\nPlease type 'Done' when you are finished adding toppings")

# while True:
#     age_input = input("\nWhat is your age? (or press D to finish) ")
#     if age_input.lower() == 'd':
#         print()
#         break
    
#     try:
#         age = int(age_input)
#         if age < 3:
#             print("Their ticket is free!")
#         elif age < 13:
#             print("Your ticket is $10")
#         else:
#             print("Your ticket is $15")
#     except ValueError:
#         print("Invalid input. Please enter a valid age or type 'Done' to finish.")


# Exercise 7-7 (Infinity Loop)

# x = 1

# while True:
#     x += 1
#     print(x)



# Exercise 7-8 (Deli), # Exercise 7-9 (No Pastrami)

# print('The deli has run out of pastrami!')

# sandwich_orders = [
#     'spicy buffalo chicken sub',
#     'pastrami',
#     'turkey, egg and cheese',
#     'pastrami',
#     'beef whopper',
#     'pastrami'
# ]


# finished_sandwiches = []

# while sandwich_orders:
#     while 'pastrami' in sandwich_orders:
#         sandwich_orders.remove('pastrami')
#     finished_sandwich = sandwich_orders.pop() 
#     finished_sandwiches.append(finished_sandwich)
#     print(f'I made your {finished_sandwich}')
# print('All sandwiches have been made!')

# print()
# print(sandwich_orders)
# print(finished_sandwiches)
# print(finished_sandwich)


# Exercise 7-10 (Dream Vacation)

# poll_results = {}   # Create empty dictionary to store polling responses
# polling_active = True   # Set polling state to active

# while polling_active:   # While polling state is active: (run the following loop)
#     name = input('Please enter your name: ')
#     dream_vacation = input('If you could visit one place in the world, where would you go? \n(Press S to see the results!) ')
#     poll_results[name] = dream_vacation

#     if dream_vacation.lower == 's':
#         polling_active = False
#         print(poll_results.items())

#         print()
#         print(poll_results)
#         print(polling_active)
#         print(dream_vacation)
#         print('\nThe poll is complete!')

#     else:
#         continue


poll_results = {} # Create empty dictionary to store polling responses
polling_active = True # Set polling state to active

while polling_active: # While polling state is active: (run the following loop)
    name = input("\nPlease enter your name: [Type 's' to see the results!] ")
    if name.lower() == 's': # If user presses s or S
        polling_active = False # Disable flag and polling state
        break
    dream_vacation = input("If you could visit one place in the world, where would you go? ")
    if dream_vacation.lower() == 's': # If user presses s or S in the dream_vacation input
        polling_active = False # Disable flag and polling state
        break
    poll_results[name] = dream_vacation # Store user input in poll_results dictionary

print('\nThe poll is complete! \nHere are the poll results: \n')
for name, vacation in poll_results.items():
    print(f"\tName: {name.title()}: \n\tDream Vacation: {vacation.title()}\n")