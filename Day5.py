# Lecture 38 😁😁////////////
# For loop with Python List

fruits = ["apple","Peach","pear"]
for frut in fruits:
    print(frut)# inside for loop print fruits element
    print(frut + "juice")# outside for loop print fruit element with juice



# lecture 39 😁😁//////////////
# Highest score

student_score = [140,234,40,44,55,66,77,88]
#otal_exam_score = sum(student_score)# Sum function add all element of list
# use max and min function to find minimum and maximum score
sum = 0
for score in student_score:
    sum +=score
print(sum)


# Find highest score 
student_score = [140,234,40,44,55,66,77,88,299]

max_score =0
for score in student_score:# score access each element of student score
    if score > max_score: #compare score and max_score
        max_score = score # here max score is a variable which store score

print(max_score) #print max score


#Lecture 40😁😁/////////////////
# For loop with  range() function
for number in range(1,10,2): # range (start,end,gap)
    print(number)#output 1,3,5,7,9


#The gauss challenge
total = 0
for num in range(1,101):
    total += num
print(total)


# Lecture 41 😁😁///////////////////
# Create a passworld Generator using Python

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','*','+']


print("Welcome to the PyPassword Generator")
n_letters = int(input("How many letters would you like in your Password?\n"))
n_symbols = int(input(f"How many symbol would you like ?\n"))
n_numbers = int(input(f"How many numbers would you like ?\n"))



password = " "

# n_letters = 4 but in range it neglect last value so
for char in range(0,n_letters):# so we add 1
    password += random.choice(letters)
 

for char in range(0,n_symbols):
    password += random.choice(symbols)

for char in range(0,n_numbers):# +1 for include total given digit
    password += random.choice(numbers)

print(password)














