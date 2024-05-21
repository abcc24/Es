#Antonio Zottola####
#19/04/2024

#8.1 write a function called display_message that prints one sentence telling everyone what you are learning about this chapter.
def display_message():
    print("Hi im studying python")
display_message()

#8.2 write a function called favorite_book() that accepts one parameter, title.
#the funcction should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(title):
    print("One of my favorite books is",title)
favorite_book("Alice in Wonderland")

#8.3 write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt.
#call the function a second time using keyword arguments.
def make_shirt(size,message):
    print(f'The size of the shirt is {size} and it has the message:{message}')
make_shirt("L","I love python")
make_shirt(message="I hate windows",size="XS")

#8.4 modify the make_shirt() function so that shirts are large by default with a message that reads i love python make a large shirt and a medium shirt with the default message, and a shirt of any size with different message.
def make_shirt(size='large', logo='I love Python!'):
    print(f"I'm going to make a {size} t-shirt.")
    print(f'It will say something like: "{logo}"')

make_shirt()
make_shirt(size='medium')
make_shirt('extrasmall', 'Live Laugh Liao')

#8.5 Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. 
#Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city,country="Canada"):
    print(f'{city} is in {country}')
describe_city("Reykjavik","Iceland")
describe_city("Toronto")
describe_city("Ottawa")

#8.6 Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city,country):
    print(f'"{city}","{country}"')
city_country("Santiago","Chile")
city_country("Ottawa","Canada")
city_country("Rome","Italy")

#8.7 Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
# Make at least one new function call that includes the number of songs on an album.
def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    print(album_dict)
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

make_album('Kanye West', 'Donda',tracks=27)


make_album('Kendrick Lamar', 'To pimp a butterfly',tracks=16)


make_album('Travis scott', 'Utopia',tracks=19)



    

#8.8 Start with your program from Exercise 8-7. 
#Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
#Be sure to include a quit value in the while loop.
def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

artist_sel="Write an artist:"
title_sel="Write a title:"
print("Enter 'Quit' anytime to stop")
while True:
    artist=input(artist_sel)
    if artist == 'Quit':
        break

    title=input(title_sel)
    if title == 'Quit':
        break

    album=make_album(artist,title)
    print(album)
 
#8.9 Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), which prints each text message.
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["hello there", "who are you", "why are you here"]
show_messages(messages)

#8.10 Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
def show_messages(messages):
    print("Showing every messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("Sending every messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "who are you", "why are you here"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("Final lists:")
print(messages)
print(sent_messages)

#8.11 Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.
def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "who are you", "why are you here"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("Final lists:")
print(messages)
print(sent_messages)

#8.12  Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time.
def sandwich():
    def make_sandwich(items):
        print("I'll make you a great sandwich:")
    for item in items:
        print(f"adding {item} to your sandwich.")
    print("Your sandwich is ready!")
    

make_sandwich('roast beef', 'cheese', 'lettuce','tomato')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

#8.13 Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
def build_profile(First_Last_Name,Age,Hair_color,Weight):
    print(f'"{First_Last_Name},Age {Age},{Hair_color} Hair,Weight {Weight}"')
build_profile("Antonio Zottola",19,"Brown","61kg")

#8.14 Write a function that stores information about a car in a dictionary. 
#The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly.
def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('Tesla', 'Y', color='blue', tow_package=False)
print(my_outback)

my_accord = make_car('Tesla', 'Y', year=2024, color='blue', height='1.624mm')
print(my_accord)

#8.15 Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
#8.16 Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *
#8.17 Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
def city_country(city,country):
    print(f'"{city}","{country}"')
city_country("Santiago","Chile")
city_country("Ottawa","Canada")
city_country("Rome","Italy")

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["hello there", "how you doin?", "what"]
show_messages(messages)

def describe_city(city,country="Canada"):
    print(f'{city} is in {country}')
describe_city("Reykjavik","Iceland")
describe_city("Toronto")
describe_city("Ottawa")

    