#Antonio Zottola
#23/04/2024

#4-1. Pizzas: Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
pizzas=["margherita","diavola","marinara"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I really like the {pizza} one")
print("I really love pizza!")

# 4.2 Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!
animal_list=["cat","dog","bear"]
for animals in animal_list:
    print(animals)

for animals in animal_list:
    print(f"a {animals} would make a great pet")
print("All these animals are cool")

#4.3 Use a for loop to print the numbers from 1 to 20, inclusive.
for x in range(1,21):
    print(x)

#4.4 Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
onemil=list(range(1,1000001))
print(onemil)

#4.5 Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.
onemil=list(range(1,1000001))
print(onemil)
print(max(onemil))
print(min(onemil))
print(sum(onemil))

#4.6  Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
odds=list(range(1,21,2))
for value in odds:
    print(value)

#4.7 Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multiple=list(range(3,31,3))
for numbers in multiple:
    print(numbers)

#4.8 A number raised to the third power is called a cube. 
#For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cubes=list(range(1,11))
for numbers in cubes:
    print(numbers**3)

#4.9 Use a list comprehension to generate a list of the first 10 cubes.
cubes_list=[value**3 for value in range(1,11)]
print(cubes_list)

#4.10 Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
print(cubes[:3])
print(cubes[2:5])
print(cubes[-3:])

# 4.11 Start with your program from Exercise 4-1. 
# Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
friend_pizzas=pizzas
pizzas.append("wurstel and chips")
friend_pizzas.append("chips")
print(f'"My favorite pizzas are:"')
for pizza in pizzas:
    print(pizza)
print(f'"My friend favorite pizzas are:"')
for pizzang in friend_pizzas:
    print(pizzang)

#4.12 All versions of foods.py in this section have avoided using for loops when printing, to save space.
# Choose a version of foods.py, and write two for loops to print each list of foods.

#4.14  Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008.
# You won’t use much of it now, but it might be interesting to skim through it.
#ah ok

#4.15 Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
pizzas=[
'margherita',
'diavola',
'marinara'
]
for pizza in pizzas:
    print(
pizza
)

for pizza in pizzas:
    print(
f"I really like the {pizza} one"
)
print(
"I really love pizza!"
)

onemil=list
(
range
(1
,1000001
))
print(onemil)

cubes_list=[
value**3 for value 
in range(
1,11
)
]
print(
cubes_list
)

# 5.1 Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.
car='srt Hellcat'
print("Is car == 'srt Hellcat'? I predict True.")
print(car == 'srt Hellcat')
print("is car == 'hundai'? I predict False.")
print(car =='hundai') 
print("is car == 'fiat'? I predict False.")
print(car =='fiat')
print("is car == 'Tesla'? I predict False.")
print(car =='Tesla')
print("is car == 'peugeot'? I predict False.")
print(car =='peugeot')
print("is car == 'honda'? I predict False.")
print(car =='honda')
car='hundai'
print("is car == 'hundai'? I predict True.")
print(car =='hundai')
car='fiat'
print("is car == 'fiat'? I predict True.")
print(car =='fiat')
car='Tesla'
print("is car == 'Tesla'? I predict True.")
print(car =='Tesla')
car='peugeot'
print("is car == 'peugeot'? I predict True.")
print(car =='peugeot')
car='honda'
print("is car == 'honda'? I predict True.")
print(car =='honda')

#5.2 You don’t have to limit the number of tests you cre-
#ate to 10. 
#If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. 
#Have at least one True and one False result for each of
#the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list
car='honda'
print(car == 'honda')
print(car!='honda')

car='honda'
print(car.lower()=='honda')

print("Numerical Test")
number=8
print(number<18)
print(number>18)
print(number!=3)
print(number==3)

print("Test Number 2")
print(number<3 and number>18)
print(number<74 and number>22)

print("Last Test The 'whether'test")
car=['hundai','volkswagen','tesla','srt hellcat']
print('srt hellcat' in car)
print('fiat' not in car)

