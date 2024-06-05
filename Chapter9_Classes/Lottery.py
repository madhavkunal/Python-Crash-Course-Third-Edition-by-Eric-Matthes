# # Exercise 9-14 (Lottery)

# from random import choices

# possible_values = [
#     "A", "B", "C", "D", "E",
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ]

# ticket = choices(possible_values, k=4)
# print(f"\n\tMy ticket is {''.join(map(str, ticket))}!")

# lottery = choices(possible_values, k=4)
# print(f"\tThe lottery is: {''.join(map(str, lottery))}!\n")

# if ticket == lottery:
#     print("It's a perfect match! Congratulations, you won the lottery!!! :)\n")
# else:
#     print("Sorry, you didn't draw the lottery this time, maybe next time. :(\n")


# Exercise 9-15 (Lottery Analysis)

from random import choices

possible_values = [
    "A", "B", "C", "D", "E",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

ticket = choices(possible_values, k=4)
print(f"\n\tMy ticket is {''.join(map(str, ticket))}!")

attempts = 1
while True:
    lottery = choices(possible_values, k=4)
    print(f"\tLottery attempt {attempts}: {''.join(map(str, lottery))}")
    
    if ticket == lottery:
        print(f"\nIt's a perfect match! Congratulations, you won the lottery after {attempts} attempt(s)!!! :)\n")
        break
    
    attempts += 1