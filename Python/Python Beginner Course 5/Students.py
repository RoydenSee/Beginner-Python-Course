class Students:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self): #when needing to use this certain function with the class it should be within the indentation
        if self.gpa >= 3.5:
            return True
        else:
            return False