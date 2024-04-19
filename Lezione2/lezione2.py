#Antonio Zottola
#18/04/2024

print("Hello World!")

#2.3 Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some python today "
name="Mario"
print(f"Hi Eric i'm {name},would you like to learn some python today?")

#2.4 Use a variable to represent a person's name and then print that person's name in lowercase,uppercase and titlecase.
lowercase=name.lower()
uppercase=name.upper()
titlecase=name.title()
print(f"{lowercase},{uppercase},{titlecase}")

#2.5 find a quote from a famous person, print the quote and the name of his author.
Albert="Albert Einstein"
print(f'{Albert} once said "A person who never made a mistake never tried something new"')

#2.6 Repeat Exercise 2.5 but this time,represent the name of the vip using a variable called: famous_name
famous_name="Kanye West"
message="My greatest pain in life is that i will never be able to see me perform"
print(f'{famous_name} once said "{message}"')

#2.8 assign the value "python_notes.txt" to a variable called filename. then use the removesuffix() method to display the filename without th fie extension, like some browsers do.
filename="python_notes.txt"
print(filename.removesuffix('.txt'))

#3.1 Store the names of a few of your friends in a list called names. print each person's name by accessing each element in the list, one at a time.
names=["antonio", "carlo","marco"]
print(names[0])
print(names[1])
print(names[2])

#3.2 Start with the list you used in Exercise 3-1, 
#but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
print(f'how are you doing {names[0]}?')
print(f'how are you doing {names[1]}?')
print(f'how are you doing {names[2]}?')

#3.3 Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
favorite_transport=["car","motorcycle"]
print(f'"i would like to own a honda {favorite_transport[1]}"')
print(f'"i would be cool to own a Volkswagen {favorite_transport[0]}"')

#3.4 If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
#Then use your list to print a message to each person, inviting them to dinner.
invites=["JayZ","Mike Tyson","DonaldJTrump"]
print(f'Dear {invites[0]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[1]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[2]}, it would be a pleasure to eat dinner with us tomorrow night.')

# 3.5 You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
print(f'{invites[1]} cannot come to dinner.')
invites2=["OJ Simpson","Queen Elizabeth"]
invites.extend(invites2)
invites.pop(1)
print(f'Dear {invites[2]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[3]}, it would be a pleasure to eat dinner with us tomorrow night.')

#3.6 You just found a bigger dinner table, so now more space is available. 
#Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
print(f'Dear {invites[0]} {invites[1]} {invites[2]} and {invites[3]}, i have found a bigger table so i will be inviting more people to it.')
invites.insert(0,"Micheal Jackson")
invites.insert(2,"Ryan Gosling")
invites.append("Jeffrey Epstein")
print(f'Dear {invites[0]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[1]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[2]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[3]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[4]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[5]}, it would be a pleasure to eat dinner with us tomorrow night.')
print(f'Dear {invites[6]}, it would be a pleasure to eat dinner with us tomorrow night.')

#3.7 You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
print("Im sorry guys but only 2 people can join for dinner")
print(f'{invites[6]} you cannot come to the dinner table for selective purpose')
invites.pop(6)
print(f'{invites[5]} you cannot come to the dinner table for selective purpose')
invites.pop(5)
print(f'{invites[4]} you cannot come to the dinner table for selective purpose')
invites.pop(4)
print(f'{invites[3]} you cannot come to the dinner table for selective purpose')
invites.pop(3)
print(f'{invites[2]} you cannot come to the dinner table for selective purpose')
invites.pop(2)
print(f'{invites[0]} you can still come if you want')
print(f'{invites[1]} you can still come if you want')
del invites

#3.8 Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.
favorite_locations=["Tokyo","Denmark","Norway","Ireland","New Zealand"]
print(favorite_locations)
print(sorted(favorite_locations))
print(favorite_locations)
print(sorted(favorite_locations,reverse=True))
print(favorite_locations)
favorite_locations.reverse()
print(favorite_locations)
favorite_locations.reverse()
print(favorite_locations)
favorite_locations.sort()
print(favorite_locations)
favorite_locations.sort(reverse=True)
print(favorite_locations)

#3.9 Working with one of the programs from Exercises 3,
#use len() to print a message indicating the number of people you’re inviting to dinner.
print(len(invites2))

#3.10 Think of things you could store in a list.
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
countries=["Italy","Romania","Greece","Vatican City","France"]
print(countries)
countries.insert(1,"Malta")
countries.append("Romania")
countries.pop(2)
del countries[3]
sorted(countries)
sorted(countries,reverse=True)
countries.reverse()
countries.reverse()
countries.sort()
countries.sort(reverse=True)

#6.1 Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live.
#You should have keys such as first_name, last_name, age, and city.
#Print each piece of information stored in your dictionary.
Information={"First Name":"Antonio","Last Name":"Zottola","Age":"19","City":"Pomezia"}

#6.2 Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.
Favorite_numbers={"Antony":"30","Luke":"12","Martin":"5"}
print(Favorite_numbers["Antony"])
print(Favorite_numbers["Luke"])
print(Favorite_numbers["Martin"])

#6.3 A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossary={"Function":"a block of code which only runs when it is called","list":"A data structure that holds an ordered collection of items","Dictionary":"A data structure that stores key-value pairs"}
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

#6.7 Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
#Loop through your list of people. 
#As you loop through the list, print everything you know about each person.
Information2={"First Name":"Mirko","Last Name":"Alessandrini","Age":"35","City":"Roma"}
Information3={"First Name":"Jordan","Last Name":"Carter","Age":"27","City":"Atlanta"}
people=[Information,Information2,Information3]
for person in people:
    print("First Name",person["First Name"])
    print("Last Name",person["Last Name"])
    print("Age",person["Age"])
    print("City",person["City"])

#6.8 Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet.
dog={"Breed":"Shiba","Owner":"Antony"}
cat={"Breed":"Sphynx","Owner":"Lucas"}
rabbit={"Breed":"American Fuzzy Lop","Owner":"Tiffany"}
pets=[dog,cat,rabbit]
for animal in pets:
    print("Breed",animal["Breed"])
    print("Owner",animal["Owner"])

#6.9 Make a dictionary called favorite_places.
#Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places={"Jacob":"Oblock","Carl":"Mountains","Amanda":"Beach"}
for word, meaning in favorite_places.items():
    print(f"{word}:\n{meaning}\n")

#6.10 Modify your program from Exercise 6-2 so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.
Antony=[15,35,40]
Luke=[74,12,34]
Martin=[32,12,68]
print(f'Antony favorite numbers:{Antony[0]}, {Antony[1]} and {Antony[2]}')
print(f'Luke favorite numbers:{Luke[0]}, {Luke[1]} and {Luke[2]}')
print(f'Martin favorite numbers:{Martin[0]}, {Martin[1]} and {Martin[2]}')

#6.11 Make a dictionary called cities.
#Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
#The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
Madrid={"Country":"Spain","Population":"3mil","Fact":"has been the capital of spain since the 17th century"}
Copenhagen={"Country":"Denmark","Population":"602k","Fact":"it is one of the oldest cities in scandinavia"}
SãoPaulo={"Country":"Brazil","Population":"12mil","Fact":"it is the largest city in brazil by population"}
cities=[Madrid,Copenhagen,SãoPaulo]
for city in cities:
    print("Country",city["Country"])
    print("Population",city["Population"])
    print("Fact:",city["Fact"])

#6.12
sumAntony=sum(Antony)
sumLuke=sum(Luke)
sumMartin=sum(Martin)

numero_piu_alto=max(sumAntony,sumLuke,sumMartin)

if numero_piu_alto==sumAntony:
    print("Antony aveva i numeri piu alti")
elif numero_piu_alto==sumLuke:
    print("Luke aveva i numeri piu alti")
else:
    print("Martin avevi i numeri piu alti")



