# Exercise 4-10

# invite_list = [
#     'Sam Altman',
#     'Marc Andreessen',
#     'Bill Gates',
#     'Steve Jobs',
#     'Mark Zuckerberg',
#     'Satya Nadella',
#     'Tim Cook'
# ]               # [0: 7] -> list index range -> 7 items total ([0] is first | [6] is last)


# print(f"\nThe first three items in the list are: {invite_list[0:3]}\n")
# print(f"\nThe middle three items in the list are: {invite_list[2:5]}\n")
# print(f"\nThe last three items in the list are: {invite_list[4:7]}\n")

# Exercises 4-11, 4-12

# my_pizza_toppings = [
#     "pepperoni and red peppers",
#     "jalapeno and banana peppers",
#     "chicken and yellow peppers",
# ]

# friend_pizza_toppings = my_pizza_toppings[:]
# # print(my_pizza_toppings)
# # print(friend_pizza_toppings)

# my_pizza_toppings.append("pineapple")
# friend_pizza_toppings.append("olives")


# print(f"\nMy favorite pizzaas are: ")
# for toppings in my_pizza_toppings:
#     print(f"{toppings}")

# print(f"\nFriend's favorite pizzaas are: ")
# for toppings in friend_pizza_toppings:
#     print(f"{toppings}")

# print()


# Exercise 4-13

#Tuple

buffet = ('Mac & Cheese', 'Garlic Breadsticks', 'Pepperoni Pizza', 'Boneless Chicken Wings', 'Greek Salad')

for food_choice in buffet:
    print(food_choice)

# Tuple items cannot be modified at the individual level

# buffet[0] = 'Ramen Noodles'
# print(buffet[0])

# Traceback (most recent call last):
#   File "C:\Users\Madhav\Desktop\Python Developer Course\Python Crash Course\Chapter4_WorkingWithLists\lists2.py", line 54, in <module>
#     buffet[0] = 'Ramen Noodles'
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# Exercise 4-14

print()

#  Overwrite Tuple - Redefine the entire tuple 

buffet = ('Ramen Noodles', 'Mozarrella Cheese Sticks', 'Pepperoni Pizza', 'Boneless Chicken Wings', 'Greek Salad')

print(buffet)

for food_choice in buffet:
    print(food_choice)

# Exercise 4-15
