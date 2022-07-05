'''
Make sure to not run the file before reading the entire code!
'''

# #Building a Translator / Encryptor
# Giraffe language
# Vowels -> g 
# ----------------

# dog -> dgg
# cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # use in to check for each letter in String
            if letter.isupper():
                translation = translation +"G"
            else:    
                translation = translation +"g"
        else:
            translation = translation + letter
    return translation



#Try/Except
try:
    answer = 10/0 
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #except a specific error 
    print(err)
except ValueError: #cataches any error in try and goes to except
    print("Invalid Input")



#Reading Files , reading , opening , parsing , closing.
employee_file = open("employees.txt" , "r") 
#r is a MODE which means read, w = write/edit, a = just appending add new info, r+ = read and write

print(employee_file.readable()) # to check if the file is read-able.
print(employee_file.read()) # showcase all infomation in the file
print(employee_file.readline()) # Just reading an individual line of the file
print(employee_file.readline()) # By using the same line again, it will read the next line. (Imagining the cursor going to the next line)
print(employee_file.readlines()[1]) #retrieving the 2nd line of the file. as it's in an array format

for employee in employee_file.readlines(): #Each line is being placed into an array format and printing each line out.
    print(employee)

employee_file.close() # Make sure to close the file after doing's what's required



# Writing to files
employee_file = open("employees.txt", "a")
#beware of appending your files do not run a second time, preventing it appending it twice.
employee_file.write("\nToby - Human Resources") 


employee_file = open("employees.txt", "w") #By changing the file name example, "employees1.txt" a new file with same content. If run-ed a second time.
#When using the W mode, instead of just appending. The entire file will be edited.
employee_file.write("\nKelly - Customer Service") 


employee_file.close()






