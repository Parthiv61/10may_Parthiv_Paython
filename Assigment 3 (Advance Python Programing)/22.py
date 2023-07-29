"""How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class """


#In Python, you can define a class using the class keyword. A class is like a blueprint that defines the structure and behavior of objects. Objects are instances of the class, and each object can have its own unique state and behavior based on the class definition.

class classname:
    # class attributes and methods
    pass



#The self parameter is a reference to the instance of the class and is automatically passed to instance methods. It allows the methods to access and modify the object's attributes.

class dog:
    name="husky"
    age=1

    def description(self):
        print("My dog name is : ",self.name)
        print("My dog age is : ",self.age)

#Object
DG=dog()
print("my dog name : ",DG.name)
DG.description()
DG.name="goldenRetriver"
DG.age=1.5
DG.description()       
    
