# # Exercise 3-1
# names = [
#     'Madhav', 
#     'Jackson',
#     'Vaanchith'
# ]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names)

# # Exercise 3-2
# print(f'Hello {names[0]}')
# print(f'Hello {names[1]}')
# print(f'Hello {names[2]}')
# print(f'Hello {names}')

# # Exercise 3-3
# cars = [
#     'Honda',
#     'Toyota',
#     'Audi'
# ]

# print(f'I would like to own a {cars[0]}')
# print(f'I would like to own a {cars[1]}')
# print(f'I would like to own a {cars[2]}')

# Exercise 3-4

# invite_list = [
#     'Sam Altman',
#     'Marc Andreessen',
#     'Bill Gates'
# ]

# print(f'{invite_list[0]}, you are cordially invited to dinner')
# print(f'{invite_list[1]}, you are cordially invited to dinner')
# print(f'{invite_list[2]}, you are cordially invited to dinner')
# print(invite_list)

# # Exercise 3-5

# print(f'{invite_list[0]} is unfortunately unable to attend')
# invite_list.remove('Bill Gates')
# invite_list.insert(0, 'Mark Zuckerberg')

# print(f'{invite_list[0]}, you are cordially invited to dinner')
# print(f'{invite_list[1]}, you are cordially invited to dinner')
# print(f'{invite_list[2]}, you are cordially invited to dinner')
# print(invite_list)

# # Exercise 3-6

# print('I have found a bigger table so I can grow our guest list!')
# invite_list.insert(0, 'Steve Jobs')
# invite_list.insert(2, 'Sundar Pichai')
# invite_list.append('Satya Nadella')

# print(invite_list)

# print(f'{invite_list[0]}, you are cordially invited to dinner')
# print(f'{invite_list[2]}, you are cordially invited to dinner')
# print(f'{invite_list[4]}, you are cordially invited to dinner')

# # Exercise 3-7

# print(f'{invite_list}, my sincerest apologies, there has been an issue with the restaurant seating and coordination and I will have to postpone the tech exec group dinner. I only have room for two right now')

# print(f'{invite_list.pop()}, my sincerest apologies, we will have to reschedule.')
# print(f'{invite_list.pop()}, my sincerest apologies, we will have to reschedule.')
# print(f'{invite_list.pop()}, my sincerest apologies, we will have to reschedule.')
# print(f'{invite_list.pop()}, my sincerest apologies, we will have to reschedule.')

# print(invite_list)

# print("Dear " + ", ".join(invite_list) + ", you are fortunately still invited as I have room for two. See you at dinner!.")

# del invite_list[0]
# del invite_list[0]

# print(invite_list)

# Exercise 3-8

# bucket_list_countries = ['Malaysia', 'Japan', 'Korea', 'Indonesia', 'Greece']

# print(f"\nOriginal bucket list: {bucket_list_countries}")

# # Sort the list alphabetically using the sorted() function (without modifying the original list)
# sorted_alphabetical = sorted(bucket_list_countries)
# print(f"\nSorted bucket list by alphabetical order: {sorted_alphabetical}")
# print(f"\nOriginal bucket list: {bucket_list_countries}")

# # Sort the list in reverse-alphabetical order using the sorted() function (without modifying the original list)
# sorted_reverse_alphabetical = sorted(bucket_list_countries, reverse=True)
# print(f"\nSorted bucket list by reverse-alphabetical order: {sorted_reverse_alphabetical}")

# # Reverse the list in-place using the reverse() method
# bucket_list_countries.reverse()
# print(f"\nReversed bucket list by reverse order: {bucket_list_countries}")
# print(f"\nOriginal bucket list: {bucket_list_countries}")

# # Reverse the list back to its original order in-place using the reverse() method
# bucket_list_countries.reverse()
# print(f"\nOriginal (re-reversed) bucket list in original order again: {bucket_list_countries}")

# # Sort the list in-place in alphabetical order using the sort() method
# bucket_list_countries.sort()
# print(f"\nPermanent sorting of bucket list by alphabetical order: {bucket_list_countries}")
# print(f"\nOriginal bucket list: {bucket_list_countries}")

# # Sort the list in-place in reverse-alphabetical order using the sort() method
# bucket_list_countries.sort(reverse=True)
# print(f"\nPermanent sorting of bucket list by reverse-alphabetical order: {bucket_list_countries}")

# Exercise 3-9

# invite_list = [
#     'Sam Altman',
#     'Marc Andreessen',
#     'Bill Gates'
# ]
# num_invited = len(invite_list)
# print(f"I am inviting {num_invited} people to dinner tonight.")

# Exercise 3-11

# invite_list = [
#     'Sam Altman',
#     'Marc Andreessen',
#     'Bill Gates'
# ]

# print(invite_list[3]) 

# Traceback (most recent call last):
#   File "C:\Users\Madhav\Desktop\Python Developer Course\Python Crash Course\Chapter3_IntroducingLists\lists.py", line 136, in <module>
#     print(invite_list[3])
#           ~~~~~~~~~~~^^^
# IndexError: list index out of range