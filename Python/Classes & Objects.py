#Classes & Objects, Basically self create a data type
class Student:
    
    def __init__(self, name, major, gpa, is_on_probation): #Defining a student, the kind of attributes a student have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

