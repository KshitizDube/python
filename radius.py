import math    
try:
    radius = int(input("what is your radius of your circle "))
    area = math.pi*(radius**2)
    print("The area of this circle is ",area)
except:
    print("The radius can only be a whole number")