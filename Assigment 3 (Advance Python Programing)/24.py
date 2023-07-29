"""Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle"""


import math
class Circle:
  
     
     def getValues(self):
          self.radius=float(input("Enter Circle's radius : "))

     def area_circle(self):
          print("Area of circle is : ", math.pi*self.radius**2)

     def perimeter_circle(self):
          print("Perimeter of circle is : ", 2*math.pi*self.radius)




#object
CR=Circle()
CR.getValues()
CR.area_circle()
CR.perimeter_circle()

    
        
     