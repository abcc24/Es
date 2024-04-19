#Antonio Zottola
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

#8.3 write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt.
#call the function a second time using keyword arguments.
def make_shirt(size,message):
    print(f'The size of the shirt is {size} and it has the message:{message}')
make_shirt("L","I love python")
make_shirt(message="I hate windows",size="XS")

#8.4 modify the make_shirt() function so that shirts are large by default with a message that reads i love python make a large shirt and a medium shirt with the default message, and a shirt of any size with different message.
def make_shirt()