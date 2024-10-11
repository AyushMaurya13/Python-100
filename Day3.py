#Lecture 22 😁//////////////////////////////////////////////////////////////////////////////////////////////////////////
#Control Flow with if / else conditional operator


print("Welcome to rollercoaster")
height = int(input("what is your height in cm ? "))

if height >=120:#if anybody is equal to 120 cm use =
    print("You can ride the rollercoaster")

# else:
#     print("sorry you have to grow taller before you can ride")
# comparision operator
#1. Equal to (==): Checks if two values are equal
#2. Not equal to (!=): Checks if two values are not equal
#3. Greater than (>): Checks if the left value is greater than the right value.
#4. Less than (<): Checks if the left value is less than the right value.
#5. Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value
#6. Less than or equal to (<=): Checks if the left value is less than or equal to the right value




#Lecture 23😁///////////////////////////////////////////////////////////////////////////////////////////////////////////
# Introduction to Modulo (%)
# modulo gives remainder
print(10%3)

#Using modulo Check the number is even or odd
number = int(input("What is the number you want to check? "))
if number % 2 == 0:
    print("Number  is Even  ")

else:
    print("Number is Odd")


#Lecture 24😁///////////////////////////////////////////////////////////////////////////////////////////////////////////
#Nested if statement and elif statements

 #if condition:
     #if another condition:
         #do this
     #else:
         #do this

 #else:
     #do this
#Example
height=int(input("What is your Height in cm "))
if height >=120:
    print("you can take ride of rollercoaster ")
    age = int(input("what is your age "))
    if age >= 18 :
        print("Please pay 40 Rs")

    else:
        print("Pay 60 Rs")

else:
    print("Sorry you have to grow taller before you can ride ")



# there are 3 cse age < 12,age = 12-18,age>18
height = int(input("What is your height in CM "))

if height >=120 :
    print("you can take a rid of rollercoaster ")
    age = int(input("What is your age "))
    if age <=12:
        print("Please Pay 20 Rs")

    elif age>12 and age<=18 :
        print("Please pay 40 Rs")

    else:
        print("Please Pay 60 Rs")

else:
    print("sorry you have to grow")



#Practice make bmi weight measurement




# Lecture 25😁/////////////////////////////////////////////////////////////////////////////////////////////////////////
# Multiple if Statement in Succession
print("Welcome to rollercoaster")
height = int(input("What is your height in Cm  "))
if height >120 :
    print("Can ride")
    age = int(input("What is your age "))

    if age >=12 and age<=18:
        bill = 40
        print("Please Pay 40 Rs ")

    elif age<12:
        bill=20
        print("Please Pay 20 Rs ")

    else:
        bill = 60
        print("Please Pay 60 Rs")

    want_photo=input("Do you want to have a photo take? Type Y for Yes and N for No.")
    if want_photo == "Y":
        bill +=3
    print(f"Your final bill is {bill}")

else:
    print("Can't ride")


#Lecture 26😁/////////////////////////////////////////////////////////////////////////////////////////////////////////
#Pizza Order Practice


# snall_pizza = 15
# Medium_pizza = 20
# Large_pizza = 25
# small_pizaa_pepperoni = 2
# large_medium_pizza_pepperoni = 3
# extra_cheese = 1

print("Welcome to Python Pizza Deliveries! ")
pizza_size = input("What size pizza do you want? S,M or L : ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N :")
extra_cheese=input("Do you want extra cheese Y or N ")
#todo : work out how much they need to pay bassed on their size choice./////// that block of code for Pizza size and price
bill = 0
if pizza_size=="S":
    bill+=15
elif pizza_size =="M":
    bill+=20
elif pizza_size=="L":
    bill+=25
else:
    print("You typed invalid input")
#todo : work out how much to add to their bill based on their pepperoni choice/////// that block of code for pepperoni

if pepperoni =="Y":
    if pizza_size == "S":
        bill +=2
    else:
        bill +=3
#todo: work out their final amount based on whether if they want extra cheese///////// that block is for extra_cheese

if extra_cheese == "Y":
    bill +=1

print(f"your final bill is {bill} :")


#Lecture 27 😁
# Logical Operator
# 1. AND: Returns True if both statements are true/
# 2.OR: Returns True if at least one of the statements is true.
# 3.NOT: Reverses the result, returns False if the result is true.


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''') # i use 3 ''' for multiple line string
# Here is some mistake Check multiple time until code is not working correct
print("Welcome to Teasure Island ")
print("Your mission is to find the treasure.")
choice =input('You are at cross road. Where do you  want to go Type "Left" OR "Right" ').lower()#dont use double quote under double quote
if choice == "left":
    s_w = input("Type swim or wait ")
    if s_w == "wait":
        which_door = input("Which Door Red,Blue,Yellow ").lower()
        if which_door == "Red":
            print("Burned by fire Game Over")
        elif which_door == "Blue":
            print("Eaten by beasts Game Over")

        elif which_door == "Yellow":
            print("You Win")

        else:
            print("Game Over")



    else:
        print("Attacked by trout Game over")

else:
    print("Fall into a hole Game Over")



#/////////////////////////////////////////////////// check it again
