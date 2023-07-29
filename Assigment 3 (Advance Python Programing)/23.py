"""Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle"""

class Rectangle:
    
    def getValue(self):
        self.length=int(input("Enter Rectangle's length : "))
        self.width=int(input("Enter Rectangle's width : "))

    def Rectangle_area(self):
        print("Area of Rectangle is : ",self.length*self.width)



#object
AR=Rectangle()
AR.getValue()
AR.Rectangle_area()

