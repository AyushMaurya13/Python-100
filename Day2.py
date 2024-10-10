print("Hello " + input("Enter Your Name \n "))
print("hello" + len(str(input("enter name\n"))))
o=int(input("enter"))
print(o)
print(type(o))
from jupyter_core.version import match

# Build a Tip Calculator
print("welcome to the tip calculator! ")
total_bill=float(input("What was the total bill? "))
given_tip=float(input("How much tip would you like to give? "))
split_bill =int(input("How many people to split the bills? "))
each_person_pay= (total_bill+given_tip)/split_bill
print("Each person should pay: " + each_person_pay )


#Lecture 14 😁
#Primitive Data Types
print(len(1234))
# The len() function is designed to return the length of a sequence (like a list, string, or tuple), not a single integer.
print("Hello"[1])
# That is  Python, subscripting refers to accessing elements of sequences like lists, tuples, and strings using square brackets []. This allows you to retrieve or modify specific elements within these sequences.
# output is H because 0 is refer to first element of strint
# we can use negative slicing [-1]
print("Hello"[-1])


# String
print("123"+"345")#conctinate 123345
print("angela")
d="ron"


# Integer (....-2,-1,0,1,2,3,4,5 upto so on)
print(1234)
print(3+5)
#large integer
print(12,34,56)#output is 12 34 56 cause comma seperate all integer
print(123_456_789)#outpu is 123456789


# Float (it contain positive negative and decimal value)
a=-1.0
b=0.0
c=1.0
print(type(a))
print(type(b))
print(type(c))

# Boolean (it contain only True and False)
print(True)
print(False)


#Lecture 15😁
# Type Error/////////// implicit conversion and explicit conversion
# len(1234)
# TypeError: object of type 'int' has no len()
# we cam measure only sequence data like string, set, dictionary
print(type("hello"))
type("hello")#type keyword is use for found which data type is use
print(type(123))
print(type(True))
print(type(1.3))


#Type casting or Type conversion
print("123"+"345")#inside the bracket there is String
print(int("12")+int("12"))#here we change string into integer we caan also use float
print(float(int(2))+int(4))# Here we change the int into float number
print(int("abs")+int("12"))#ValueError: invalid literal for int() with base 10: 'abs'

print("Number of letters in your name:"+(len(input("Enter your name\n"))))#len function is only use with only with integer
print("Number of letters in your name:"+(len(input("Enter your name\n"))))#we convert the len into string

name_of_the_user = input("Enter Your Name")
length_of_name = len(name_of_the_user)
print(type("Number of letters in your name "))#<class 'str'>
print(type(length_of_name))#<class 'int'>
print("Number Of letters in your name:" + "")# we can't add int and str
print("Number of letter in your name "+str(length_of_name))



#Lecture 16😁
#Mathematical Operation in Python
print("my age: "+str(12))
print(12+34)
print(9-4)
print(2*3)
print(5/2)# it always return float number
print(5//2)#it is floor division remove value from decimal
print(3**2)#exponent means 3 two times


#PEMDAS left to right calculation/////priority
# ()
# **
# * OR /
# + OR -
print(3*3+ 3/3-3)#whenever we use divide it always give value in float 6.0




# Exercise BMI Calculator body mass index
height=float(input("Enter your Height in Meter\n"))
weight =float(input("Enter Your Weight in KiloGram\n"))
bmi=weight/(height**2)
print("Your BMI (Body Mass Index is) :" , bmi)

if(bmi>0 and bmi <= 18.5):
    print("Your are in : Underweight")

elif(bmi>18.5 and bmi<=25):
    print("You are in : Normal")

elif(bmi>25 and bmi<=30):
    print("You are in : Overweight")

else:
    print("You are In Obesity Categories")



#Lecture 17 😁
# Number Manupulation and F String in Python
#Sure! Python offers a variety of ways to manipulate numbers. Here are some common techniques and functions:

#Basic Arithmetic Operations
#Addition: a + b
#Subtraction: a - b
#Multiplication: a * b
#Division: a / b
#Integer Division: a // b
#Modulus: a % b
#Exponentiation: a ** b
#Built-in Functions
#abs(x): Returns the absolute value of x.
#round(x, n): Rounds x to n decimal places.
#pow(x, y): Returns x raised to the power y.
#int(x): Converts x to an integer.
#float(x): Converts x to a floating-point number.



bmi = 84/1.65**2
print(bmi)
print(int(bmi))#convert float into int

print(round(bmi))#round function round up or down
print(round(3.4))#output is 3 cause less than 0.5
print(round(3.6))#output is 4 cause greater than 0.5
# we heard round off in money
print(round(bmi,2)) # Here 2 means only two digit after decimal
score= 0
score +=1# += it operator means score = score+1
print(score)



# f-string
score = 0
height=1.8
is_winning = True
name="ayush"
print(f"your Score is = {score},your height is={height},You are winnig is:{is_winning}  ")
print(f"My name is={name}")



# Tip calculator Project
print("Welcome to the tip calculator!")
total_bill= float(input("What was the total bill? Rs. ") )#By default input is string
tip=int(input("How much tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))

# calculate percentage
# 200 ka 10 %
#e=(250*20)/100
#print(e)

#Logic
bill_with_tip=(total_bill * tip)/100 + total_bill
print(f"Total ammount is : {bill_with_tip} Rs")

#We can calculate separate each person money//////////////////////////// Make same program step by step lecture 18 14 minute
print(f"Each Person should Pay : {bill_with_tip/people } Rs ")