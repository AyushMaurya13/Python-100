#Printing to the console 
#Write Your code beloew
"""In between the double quote 
 that is not code that is some text 
that i wanted to print """

print("Hello World!")
#These text in programming lango is known as String(Collection on Charecters)


print("hello world")
#SyntaxError: unte^rminated string literal (detected)
# That means you are Not putting a " before the end of the line
#Use if You want to comment



# Coding Exercise-1 Printing Practice
#👍Lecture No. 6
#Write a program that uses print statements to print the following recipe into the Output console.
# 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# 2. Knead the dough for 10 minutes.
# 3. Add 3g of Salt.
# 4. Leave to rise for 2 hours.
# 5. Bake at 200 degrees C for 30 minutes.
print("1. Mix 500 of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 300 degrees C for 30 minutes.")






#👍Lecture No. 7 String Manipulation
# Fix the code below 👇
#Debugging Practioce
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")




#👍lecture No.8 input function
input("what is your name?")
print("Hello " + input("What is your name"))
#there are 2 parenthises one is for closing and othe ris for input funtion
#use + sign for concatenation
print("Hello " + input("what is your name?") +"!")




#👍Lecture 9
# python Variable
name=input("What is your name?")
#there is a variable that is name it contain
print(name)
# in computer there are multiple number variable help to give the a name of perticular number
name = "Angela"
print(name)
# variable can be change and varryed
name = "Ayush"
print(name)




#how to count lenth of A String
#String Length
name = "Angela yu"
print(len(name))
#output is 9 because of an indentation gap between Angela And yu
name = input("Enter your name")
print("Your name is:" + name)


# print("Length of your Name is:" + len(name))#typeError  can only concatenate str (not "int") to string
# Use tpye casting
print("Length of your name is:" + str(len(name )))
print(len(input("What is your name")))#but we dont use this method


#we usethis formate
username = input("what is your name?\n")
length = len(username)
print(length)


#question is that why we cannn't perform mathematical operation without declare data type
num1=int(input("Enter a Number " + " "))
num2 = int(input("Enter second Number"+" "))
product=num1*num2
print(product)
print("Hello " +len(str(input("Enter your namme "))))


# 👍Lecture 10
# How to create a variable in python
# use (a-z) and (A-Z) in starting and underscore(_)
Name = " ayush"
name ="angela mam"
my_name = "ayush"
_name = "soul"


#We dont use numeric first during variable declaration
# 1name="name"
# 1_name="name"

# 👍Lecture 11
#Brand name Generator
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city grew up in ?\n")
pet_name = input("What's your pet's name\n")
print("your band name could be :" + city_name+" "+  pet_name)



