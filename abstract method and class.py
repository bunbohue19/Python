"""

A class is called an Abstract class if it contains one 
or more abstract methods.

An abstract method is a method that is declared, but
contains no implementation.

Abstract classes may not be instantiated, and its abstract 
methods must be implemented by its subclasses.


Python comes with a module which provides the base for defining
Abstract Base classes (ABC) and that module name is ABC.

A concrete class which is a sub class of such abstract base class
that implements the abstract base by overriding its abstract methods.

"""

# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class Mother(ABC):
    
    @abstractmethod         # defining
    def one(self):    
        pass
    
    def two(self):
        print("concrete class")
        
class Daughter(Mother):
    
    def one(self):
        print("Abstract class")
    
obj = Daughter()
obj.one()
obj.two()



    
        