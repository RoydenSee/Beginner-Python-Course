#Getting input from users
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are" + age )

#Building a basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) 
#without changing datatypes the two variables will concat as strings, float to take in consideration to decimals
print(result)

#Mad lips games
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue.")
print(celebrity + " is beautiful")
print("But so are you.")

#Lists
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Roland", "Laurel", "Galande", "Kelly", "Harman", "Benson", "Enrique", "Blanche"] #Last Fortress Heroes
            #0        #1      #2       #3        #4           #5          #6 / -2   #7 / -1
print(friends[0]) #printing item in list / -1 Last item of the list
print(friends[1:3]) # printing a few items of the list in order
friends[5] = "Marlen" #Replacing item in the list
print(friends)
#List Functions
friends.extend(lucky_numbers) #adding two list together
friends.append("Roger") #Add to the end of the list
friends.insert(14, "Benson") #insert element inbetween while the rest is pushed back.
friends.remove("Marlen") #Remove element in list
#friends.clear() #clear entire list 
#friends.pop() #Remove last element of the list
friends.index("Roland") #To check if a certain element in the list
friends.count("")
friends.sort() #Sort in alphbetical order and numerical order
lucky_numbers.reverse() # Reverse the order of the elements in the list
friends2 = friends.copy() # Copy the same elements in a list into another list.
print(friends)

#Tuples : tuples can't be changed or modified unlike list, used in special situations like fixed data.
coordinates = (4, 5)
print(coordinates[0]) # The elements can be accessed in the tuple 

#Functions
def say_hi(name, age): # A function with 2 parameter required to call the function
    print("Hello " + name + " , you're " + str(age))

say_hi("Roland", 35) #To execute / call the function

#Return Statement
def cube(num):
   return num*num*num #return the value which have a logic unlike just printing

result = cube(3)
print(result)

#If Statements: Have a condition, if true execute, if false do sth else or stop.
is_male = True
is_tall = True

if is_male or is_tall: #if either of the condition is true it will print
    print("You're a male or tall or both")
elif is_male and not(is_tall): # True to male but false to being tall. the function not() is to make the variable False.
    print("You're neither a male nor tall") 
if is_male and is_tall: #Both conditions must be True for it to print.
    print("You're a tall male")
else:
    print("You're not a male and not tall")

#If Statements and Comparisons
def max_num(num1, num2, num3): #Comparison Operators: >= <= == 
    if num1 >= num2 and num1 > num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,19,9))
