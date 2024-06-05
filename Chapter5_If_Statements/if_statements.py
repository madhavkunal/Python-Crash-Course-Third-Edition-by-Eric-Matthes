# # Exercise 5-1 & 5-2 (Conditional Tests)

# food = 'apple pie'

# if 'Apple Pie'.lower() == 'apple pie':
#     print('This is True')

# print(1 < 5)  # True
# print(1 > 0)  # True

# if 1 < 5 and 2 < 5:
#     print('both statements are correct')

# if 1 < 5 or 2 < 5:
#     print('both statements are correct')

# if 1 < 0 and 2 < 5:
#     print('both statements are incorrect')

# if 1 < 0 or 2 < 0:
#     print('both statements are incorrect')

# snacks = [
#     'cheetos',
#     'doritos',
#     'chips ahoy'
# ]

# if 'cheetos' in snacks:
#     print('correct')

# if 'fritos' not in snacks:
#     print('correct')

# print(food == 'apple pie')  # True
# print(food != 'chocolate mousse')  # True
# print('apple pie' == 'apple pie')   #True 


# print(1 == 1)  # True
# print(1 >= 1)  # True
# print(1 <= 1)  # True
# print(1 != 0)  # True

# print(food == 'chocolate mousse')  # False
# print(food == 'apple_pie')  #False

# print(1 == 0)  # False
# print(1 >= 2)  # False
# print(1 <= 0)  # False
# print(1 != 1)  # False



# Excercise 5-3, 5-4, 5-5 (Alien Colors)

# alien_color = 'green'
# # alien_color = 'yellow'
# # alien_color = 'red'

# if alien_color == 'green':
#     print('You just earned 5 points!')
# elif alien_color == 'yellow':
#     print('You just earned 10 points!')
# elif alien_color == 'red':
#     print('You just earned 15 points!')



# # if alien_color == 'yellow':
# #     print('You just earned 15 points!')


# Exercise 5-6 (Stages of Life)

# # age = 1 # person is a baby
# # age = 2 # person is a toddler
# # age = 4 # person is a kid
# age = 13 # person is a teenager
# # age = 20 # person is an adult
# # age = 65 # person is an elder

# if age < 2:
#     print('person is a baby')
# elif age < 4:
#     print('person is a toddler')
# elif age < 13:
#     print('person is a kid')
# elif age < 20:
#     print('person is a teenager')
# elif age < 65:
#     print('person is an adult')
# else:
#     print('person is an elder')        


# Exercise 5-7 (Favorite Fruit)

# favorite_fruits = [
#     'oranges',
#     'watermelon',
#     'blueberries'
# ]

# if 'oranges' in favorite_fruits:
#     print('You really like oranges, huh')

# if 'watermelon' in favorite_fruits:
#     print('You really like watermelon, huh')

# if 'blueberries' in favorite_fruits:
#     print('You really like blueberries, huh')

# if 'apples' in favorite_fruits:
#     print('You really like apples, huh')

# if 'strawberries' in favorite_fruits:
#     print('You really like strawberries, huh')


# Exercise 5-8 (Hello Admin), 5-9 (No Users), 5-10 (Checking Usernames)

# current_users = [
#     'admin',
#     'Madhav',
#     'Mom',
#     'Dad',
#     'guest'
# ]

# new_users = [
#     'madhav',
#     'mom',
#     'Vaanchith',
#     'Varshita',
#     'Jackson'
# ]

# # users = []  # prints We need to find some users!
# # current_users = 'admin' # prints Hello admin, thank you for logging in again.
# # users = 'Madhav' # prints Hello Madhav, thank you for logging in again.
# # new_users = 'Bob'

# for user in new_users:
#     if user.lower() in [user.lower() for user in current_users]:  # list comprehension
#         print(f' The username {user} has been used already. Please enter a new username.')
#     else:
#         print(f'The username {user} is available!')

# if current_users:
#     print(f'Hello {current_users}, thank you for logging in again.')
# elif current_users == 'admin':
#     print('Hello admin, would you like to see a status report?')
# else:
#     print('We need to find some users!')


# Exercise 5-11 (Ordinal Numbers)

ordinal_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

for number in ordinal_numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    elif number == 4:
        print('4th')
    elif number == 5:
        print('5th')
    elif number == 6:
        print('6th')
    elif number == 7:
        print('7th')
    elif number == 8:
        print('8th')
    elif number == 9:
        print('9th')


        

