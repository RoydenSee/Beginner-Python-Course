# importing of math functions, * could be define as all
from math import *
# 1st print Statement
print("Hello World\n")
# print shapes
print("   /|")
print("  / |")
print(" /  |")
print("/___|\n")
# Variables and Data Types
character_name = "Jace"
character_age = "70"
print("There once was a lady named " + character_name + ".")
print("She was " + character_age + " years old.")
print("She really liked the name " + character_name + ".")
print("But didn't like being " + character_age + ".\n")
# Working with Strings
phrase = "Umbrella Academy"
print(phrase + " is cool.\n") # concatnation & "\n" = next line
print(phrase.upper()) #Change all to upper case
print(phrase.upper().isupper()) #Check true or false that phrase is all in caps
print(len(phrase)) #length of phrase
print(phrase.index("U")) # 0 will be shown
print(phrase.replace("Umbrella" , "My Hero no")) #replacing a string of word with another
#Working with numbers 
print(3.14159265359) # Whole number (int) or decimals (float)
value = 5 * 3 / 3 + 4 - (2 + 1)  #BODMAS Rules Applies in 
print(value % 4) # % (modules) finding remainder ... value = 6.
print(str(value) + " is my lucky number") # int have to change datatypes to concatnate with string.
print(abs(value)) # absoulute of value
print(pow(value , 2)) # value power to 2
print(max(4,6)) # find max value in the parenthesis
print(round(3.7)) # round-up / down the number in the parenthesis
# from math import *
print(floor(3.7)) # Round down regards of value more than 0.5
print(ceil(3.4)) # Round up regards of value less than 0.5
print(sqrt(36)) # Find Square root of value
