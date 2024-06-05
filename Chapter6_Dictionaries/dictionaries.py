# Exercise 6-1, 6-2 (Person, Favorite Numbers)

# friend = {
#     'first_name': 'Kwame',
#     'last_name': 'Jackson',
#     'age': 33,
#     'city' : 'Jersey City'
# }

# print(friend)
# print(friend['first_name'])
# print(friend.get('last_name'))
# print(friend.get('middle_name'))

# favorite_numbers = {
#     'madhav': 5,
#     'jackson': 7,
#     'vaanchith': 9,
#     'mom': 10,
#     'dad': 2
# }

# print(favorite_numbers)
# print(favorite_numbers.items())
# print(favorite_numbers['madhav'])

# # Printing key-value pairs using items()
# for key, value in favorite_numbers.items():
#     print(f"Name: {key.title()}, Favorite Number: {value}")


# Exercise 6-3, 6-4 (Glossary)

# python_glossary = {
#     list: [],
#     tuple: (),
#     dict: {},
#     str: ''
# }

# print(python_glossary)  # {<class 'list'>: [], <class 'tuple'>: (), <class 'dict'>: {}}

# for key, value in python_glossary.items():
#     print(key, value)


# Exercise 6-5 (Rivers)

# rivers = {
#     'nile river': 'egypt',
#     'yangtze river': 'china',
#     'amazon river': 'brazil'
# }

# for river, country in rivers.items():
#     print(f'The {river.title()} runs through {country.title()}')


# Exercise 6-6 (Polling)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

# friends = [
#     'madhav',
#     'andrei',
#     'jen',
#     'sarah'
# ]

# for friend in friends:
#     if friend in favorite_languages.keys():
#         print(f'{friend.title()}, thank you for taking the poll!')
#     else:
#         print(f'{friend.title()}, please take a poll of favorite programming languages!')

 
# Exercise 6-7 (People)

# friend = {
#     'first_name': 'Kwame',
#     'last_name': 'Jackson',
#     'age': 33,
#     'city' : 'Jersey City'
# }

# friend2 = {
#     'first_name': 'Vaanchith',
#     'last_name': 'Venkatesh',
#     'age': 27,
#     'city' : 'Basking Ridge'
# }


# friend3 = {
#     'first_name': 'Mihir',
#     'last_name': 'Kunal',
#     'age': 33,
#     'city' : 'New York City'
# }

# people = [friend, friend2, friend3] #list of dictionaries

# for friend in people:
#     print(f"\n{friend['first_name']} {friend['last_name']} is {friend['age']} years old and lives in {friend['city']}.") 
# print()


# Exercise 6-8 (Pets)

# pet = {
#     'name': 'Sumo',
#     'animal type': 'cat',
#     'owner': 'Madhav',
# }

# pet2 = {
#     'name': 'Byron',
#     'animal type': 'dog',
#     'owner': 'Jackson',
# }

# pets = [pet, pet2] #list of dictionaries

# for pet in pets:
#     print(f"\n{pet['owner']} owns a {pet['animal type']} named {pet['name']}.") 
# print()

# Exercise 6-9 (Favorite Places)

# favorite_places = {
#     'Madhav': 'Greece',
#     'Jackson': 'Cuba',
#     'Vaanchith': 'Spain'
# }

# print()
# for person, place in favorite_places.items():
#     print(f"{person}'s favorite plave to visit is {place}!")
# print()

# Exercise 6-10 (Favorite Numbers)

# favorite_numbers = {
#     'madhav': [5, 2],
#     'jackson': [7, 3],
#     'vaanchith': [9, 11],
#     'mom': [10, 23],
#     'dad': [2, 56]
# }

# # Printing key-value pairs using items()
# for person, numbers in favorite_numbers.items():
#     print(f"Name: {person.title()}, Favorite Numbers: {numbers}")

cities = {
    'Los Angeles': {
        'country': 'United States',
        'population': '3.9 Million People',
        'fact': 'Los Angeles is known for its Mediterranean climate, ethnic and cultural diversity, and the Hollywood entertainment industry. It is the second-most populous city in the United States, after New York City.'
    },

    'Tokyo': {
        'country': 'Japan',
        'population': '13.96 Million People',
        'fact': "Tokyo is the capital and largest city of Japan. It is known for its vibrant urban culture, advanced technology, efficient public transportation system, and a blend of modern and traditional architecture. Tokyo is also the world's largest metropolitan economy."
    },

    'Crete': {
        'country': 'Greece',
        'population': '636,000 People',
        'fact': 'Crete is the largest and most populous of the Greek islands. It is known for its ancient Minoan civilization, which flourished during the Bronze Age. The island is also famous for its beautiful beaches, rugged landscapes, and delicious cuisine, including dishes like moussaka and dakos.'
    },
}

for city, city_info in cities.items():
    print(f"\n{city}, {city_info['country']}, has a population of {city_info['population']}. {city_info['fact']}")
print()