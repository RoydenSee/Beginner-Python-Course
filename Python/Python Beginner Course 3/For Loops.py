# # For Loops
for letter in "Umbrella Academy": #for loop in a String
    print(letter)

friends = ["Roland", "Laurel", "Galande", "Kelly", "Harman", "Benson", "Enrique", "Blanche"]
for name in friends: #for loop in an Array
    print(name)
for index in range(len(friends)): #printing elements in the array using a for loop 
    print(friends[index])


for index in range(10): #print numbers from 0 - 9 , 
    print(index) 


for index in range(5):
    if index == 0:
        print(str(index) + " is the first iteration")
    else:
        print("The next iteration is " + str(index))



#2D Lists & Nested Loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1]) #column and row, both being [0,1,2] order 

for row in number_grid: #Getting each element in the 2D List by using nested for loop
    for col in row:
        print(col)