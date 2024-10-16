# Lecture 31😁///////////////////////////////////////////////////////////////////
# Random Module
# random is use for generate random variable

# import random
# random_num=random.randint(0,1)#  random(), which generates a random float uniformly in the half-open range 0.0 <= X < 1.0.
# if random_num == 0:
    # print("Tail")

# else:
    # print("Head")

# print(random_num)





#Lecture 32😁 //////////////////////////////////////////////////////////////////
# Understanding the offset and Appending Items to list
# List *****
# state_of_india =["UP","Bihar","Uttrakhand","Delhi"]
# print(
# state_of_india)
# print(state_of_india[0])# use [0,1,2,3.....] bracket for acess element from list through the index
# print(state_of_india[-1])#Negative index use to acess last item of list
# print(state_of_india[1])
#print(state_of_india[1][2])#it access 2nd items 2 index


# state_of_india[1] = "Rajasthan"
# print(state_of_india)

# state_of_india.append ("West Bengal")# use append to add item in last of list
# state_of_india.extend(["rampur","Parasni"])
# print(state_of_india)



#Lecture 33 😁////////////////////////////////////
# Who will pay the bill
# import random
# friends=["adarsh","ayush","Prashant","vasu","gulsan"]
#
# 1st option
# print(random.choice(friends))#random.choice us for sequence we can say char
# 2nd option

# random_index = random.randint(0,4)
# print(friends[random_index])
#
#

#Lecture 34😁/////////////////////////////////////////
#Index error and working with Nested list
# states_of_india = ["Bombay","Madras","Bengal","Assam","Bihar", "Orissa"]
# print(states_of_india[10])#IndexError: list index out of range

#Nested List

# fruits = ["mango","Apple","Banana","Grapes","Orange"]
# vegitable = ["Tomato","Potato","Ladyfinger"]
# total_item = [fruits,vegitable]
# print(total_item)#list= [['mango', 'Apple', 'Banana', 'Grapes', 'Orange'], ['Tomato', 'Potato', 'Ladyfinger']]
# print(total_item [1][1]) # it access 'potato' list vegitable.
# print(total_item[1][2]) #it access 'ladyfinger' list vegitable.
# print(total_item[0][1]) #it access 'apple' list fruits cause [0].


# Rock Paper scissors*************


import random # Please Check and understand it 

rock = '''
    ________
___'    ____)
        (____)
        (____)
        (____)
        (___)
---.____
'''
paper = '''
    ________
___'    ____)____
        (________)
        (__________)
        (_______)
        (______)
---.____
'''

scissors = '''
    ________
___'    ____)____
        (________)
        (__________)
        (_____)
        (____)
---.____
'''

game_images = [rock ,paper,scissors]


user_choice = int(input("What do you choose ? Type 0 for Rock 1 for paper or 2 for Scissors\n"))
print(f"You Chose {user_choice} ")
print(game_images[user_choice])


compuer_choice = random.randint(0,2)
print(f"Computer Chose {compuer_choice}  ")
print(game_images[compuer_choice])


if user_choice >= 3 or compuer_choice < 0:
    print("You type an invalid Number You lose ")

elif user_choice == 0 and compuer_choice == 2:
    print("You win")

elif compuer_choice == 0 and user_choice == 2:
    print("you lose ")

elif compuer_choice > user_choice:
    print("You Lose!")

elif user_choice > compuer_choice:
    print("You win")

elif compuer_choice == user_choice:
    print("It's Draw")

else:
    print("You type invalid number")


  











