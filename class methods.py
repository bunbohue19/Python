"""
Classmethod can be access from any instance or any class.

If we want to make a method that can be accessed by instance
as well as class and the argument which we pass and we don't 
want to take self then we use classmethod
"""

class Student():
    no_of_subjects = 5
    
    def __init__(self, name, section, marks):
        self.name = name
        self.section = section
        self.marks = marks
    
    def details(self):
        return f"Name is {self.name}, section is {self.section} and marks are {self.marks}"
   
    @classmethod
    def change_subjects(cls, leaves):
        cls.no_of_subjects = leaves
        
one = Student("Rita", "A", 34)
two = Student("Rohan", "B", 21)

print(one.no_of_subjects) 
Student.change_subjects(15)
print(one.no_of_subjects)

