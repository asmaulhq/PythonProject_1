
"""
character_name = "Tom"
character_age = 50
is_male = True
print("There was an man called "+character_name+", ")
print("he is "+str(character_age)+" years old.")

character_name = "Mike"
print("He liked him name "+character_name+",")
print("but does not like being "+str(character_age)+".")

print("ABC Academy")
print("ABC \nAcademy")
print("ABC \"Academy")
phrase = "ABC Academy"

print(phrase + "is cool")

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[2])
print(phrase.index("Acad"))
print(phrase.count("A"))
print(phrase.replace("ABC", "XYZ"))

print(3*(4+5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num) + " is my favorite number")

my_num2 = -7
print(abs(my_num2))

print(pow(4, 6))
print(max(4, 8))
print(min(4, 8))
print(round(5.19))

from math import *
print(sqrt(36))
print(floor(3.69)) # chop off after .
print(ceil(3.169)) # round no matter what .
"""
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello "+name.capitalize()+"! You are "+str(age))
"""

# Build basic calculator
"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) #int(num2)
print(result)
"""

# Mad Libs Game
"""
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are "+color)
print(plural_noun+ "  are blue")
print("I love "+celebrity)
"""
# Homework: Create your own game

# List | Array
"""
friends = ["Kevin", "Jim", "Tom", "Oscar", "Peter"]
friends[1] = "Mike"
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
print(friends[1])
"""

# Function
"""
luck_number = [49, 8, 15, 16, 23, 42]
friends = ["Kevin", "Jim", "Tom", "Oscar", "Peter", "Oscar"]
friends.extend(luck_number)
friends.append("Jerry")
friends.insert(1, "Joe")
friends.remove("Jim")
#friends.clear()
#print(friends)
friends.pop() # remove last item from the list
print(friends.index("Kevin"))
print(friends.count("Oscar"))

luck_number.sort()
print(luck_number)
luck_number.reverse()
print(luck_number)

friends2 = friends.copy()
print(friends2)
"""

#Tuples: Similar to list/array but can't change/modify later
"""
coordinates = (4, 5) # can't change anywhere else
coordinates2 = [(4, 5) , (8, 98), (43, 9)  ]
# coordinates[1] = 10 # can't do this
print(coordinates[1])
print(coordinates2[1][1])
"""

#Function: name should in lower / seperated by _
"""
def welcome_user(name, age):
    print("Helo "+ name + ". You are " + str(age))

print("Top")
welcome_user("Mike", 22)
welcome_user("Asmaul", "33")
print("Bottom")
"""

# Return Statement
"""
def cube(num):
    return num*num*num
   # print("code") # Not doable

result = cube(5);
print(cube(4))
print(result)
"""

#If Statements
"""
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and tall.")

elif  is_male and not(is_tall):
    print("You are a male but not tall.")
elif  not(is_male) and is_tall:
    print("You are a not male but tall.")
else:
    print("You are neither male or nor tall.")
"""

# If Statements and Comparison operator
"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(581, 8, 3))
"""

#Building a Better Calculator
"""
num1 = float(input("Enter a number: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter another number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator.")
"""
# Dictionaries
"""
month_conversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    5: "Five",
    6: "Six",
    7: "Seven"
}

print(month_conversion["Mar"])
print(month_conversion.get("Dec"))
print(month_conversion.get("Luv", "Not a valid key"))
print("Dec" in month_conversion)
print(month_conversion[5])
"""

# While Loop
"""
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")
"""
#Building guessing game
"""
secret_word = "banana"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose.")
else:
    print("You win!")
    
"""
# For loop
"""
for letter in "ABC Academy":
    print(letter)

friends = ["Kevin", "Jim", "Tom", "Oscar", "Peter", "Oscar"]

for friend in friends:
    print(friend)

for index in range(len(friends)):
    if index == 0:
        print("First friend")
    else:
        print(friends[index])
"""

# Exponent Function
"""
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4, 3))
"""

# 2D List and Nested Loops
"""
numbers_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(numbers_grid[2][1])

for row in numbers_grid:
    for col in row:
        print(col)
"""
# Build a Translator
"""
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
"""

# Comments
# This program is fun
#print("Comments are fun!")

"""
This is 
a multi-line 
comment"""

# Try Except
"""
try:
    input_value = int(input("Enter a number: "))
    print(input_value)
    num1 = 10/0
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid input")
"""

# Reading Files

# r=read, w=write; a=append; r+ = read & write
"""
employees = open("employees.txt", "r")

#print(employees.readable())
#print(employees.read())
#print(employees.readlines()[2])
#print(employees.read(10))
for employee in employees.readlines():
    print(employee)
employees.close()
"""

# Writing to Files / creating new files
"""
employees = open("index.html", "w") #open("index.html", "a") for adding to existing file
employees.write("<p>This is HTML</p>")
employees.close()
"""

#Module and Pip: Modules are like WordPress plugins. Use any external or in-build modules as needed
"""
import usefull_tools
print(usefull_tools.generate_random_integer(4, 98))
print(usefull_tools.generate_random_float())

import docx
print(docx)
print("python-docx is working!")
"""

# Classes and Objects : We can create our own custom datatype using this similar to STRING, INT, BOOLEAN etc
"""
from Student import StudentObject

student1 = StudentObject("Mike", "Business", 3.1, False)
student2 = StudentObject("John", "Art", 3.8, True)

print(student1.gpa)
"""
"""
from Student import Phone
phones = [
    Phone("Apple", "iPhone 11", "Silver", "61000", "110", "100"  ),
    Phone("Apple", "iPhone 16", "Black", "89000", "118", "50"),
    Phone("Samsung", "Galaxy S20", "Blue", "16000", "1.8", "1000"  )
]
print("Brand \t\t Model \t\t Color \t\t Price \t\t Weight \t\t Quantity \n------------------------------------------------------------------------")
for phone in phones:
    print(phone.brand + "\t\t"+ phone.model + "\t\t"+ phone.color + "\t\t"+phone.price + "\t\t"+phone.weight+"gm" + "\t\t"+phone.count)

"""

#Building a multiple choice quiz
"""
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Yellow\n(b) Red\n(c) Green\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+" out of "+str(len(questions))+" correct.");


run_test(questions)
"""

# Object Functions
"""
from Student import StudentObject
student1 = StudentObject("Mike", "Business", 3.1, False)
student2 = StudentObject("John", "Art", 3.8, True)
print(student1.on_honor_roll())
"""

#Inheritance
from Chef import Chef
from Chineschef import ChinesChef
my_chef = Chef()
my_chef.make_special_dish()

my_chinesechef = ChinesChef()
my_chinesechef.make_special_dish()

# Python Interpreter
