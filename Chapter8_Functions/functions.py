# # Example 8-3 (T-Shirt), # Example 8-4 (Large Shirts)

# def make_shirt(size = "Large", message = "I love Python"):  # Define function call with paramaters size and message that have default values of "Large" and "I love Python" respectively
#     print(f"You have to make a {size} size shirt with the words: {message}")    
#     # Print statement that is dynamic based on the arguments given

# make_shirt('Medium', 'Kobe')    # Call function with positional arguments
# make_shirt(size = "Medium", message = "Kobe")   # Call function with keyword arguments
# # Both print statements read: You have to make a Medium size shirt with the words: Kobe
# make_shirt()    # print statement reads: You have to make a Large size shirt with the words: I love Python
# make_shirt("Medium")    # print statement reads: You have to make a Medium size shirt with the words: I love Python

# # Example 8-5 (Cities)

# def describe_city(city, country = "United States"):
#     print(f"{city} is in {country}")

# describe_city("New York City")
# describe_city("Miami")
# describe_city(city = "Tokyo", country = "Japan")


# Example 8-6 (City Names)

# print()
# def city_country(city, country):
#     print(f"{city.title()}, {country.title()}")

# city_country("santiago", "chile")
# city_country("Miami", "United States")
# city_country("Tokyo", "Japan")
# print()


# Example 8-7 (Album)

# def make_album(artist, album, song_count = None):
#     if song_count:
#         album_info = {'Artist Name': artist.title(), 'Album Name': album.title(), 'Song Count': song_count}
#     else:
#         album_info = {'Artist Name': artist.title(), 'Album Name': album.title()}
#     return album_info

# print(make_album("SZA", "SOS", 23))
# print(make_album("Taylor Swift", "Midnights"))
# print(make_album("Paramore", "This Is Why", "10"))




# Example 8-8 (User Albums)



# def make_album(artist, album, song_count = None):
#     if song_count:
#         album_info = {'Artist Name': artist.title(), 'Album Name': album.title(), 'Song Count': song_count}
#     else:
#         album_info = {'Artist Name': artist.title(), 'Album Name': album.title()}
#     return album_info

# while True:

#     print("\n\t*Please enter 'q' at any time to quit*")

#     artist = input("Who is your favorite artist? ")
#     if artist == 'q':
#         break

#     album = input("What is your favorite album from them? ")
#     if album == 'q':
#         break

#     song_count = input("How many songs are in the album? ")
#     if song_count == 'q':
#         break

#     formatted_album = make_album(artist, album, song_count)
#     print(formatted_album)



# Example 8-9 (Messages), Exercise 8-10 (Sending Messages), Exercise 8-11 (Archived Messages)

# text_messages = [
#     "Hi",
#     "How are you?",
#     "Good, yourself?",
#     "I'm great, thanks."
# ]

# sent_messages = []

# def show_messages():
#     for message in text_messages:
#         print(text_messages)
#         break

# def send_messages():
#     for message in text_messages:
#         print(f"\tmessage: {message}")
#         sent_messages.append(message)


# # show_messages()
# # send_messages()
# # print(text_messages[:])
# # print(sent_messages)
# print(text_messages)
# print(sent_messages)
# send_messages()
# print(text_messages)
# print(sent_messages)
















# def add_numbers(a, b):
#     result = a + b
#     print("Inside the function: ", result)

# sum = add_numbers(5, 3)
# print("Outside the function: ", sum)


