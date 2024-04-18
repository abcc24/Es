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
invites.insert(2,"")