#using python function code and user input calculate the surface area
#of a cylinder. if the radius is 10m and the height is 15m. if pie equals
#to 3.142. print out the result. hint:2*pie*r*h+2*pie*r*r

def calculatecylinder():
    pie=3.142
    print("enter your radius")
    r=float(input())
    print("enter your height")
    h=float(input())
    surfarea=2*pie*r*h+2*pie*r*r
    print("this is the area of a cylinder",surfarea)
calculatecylinder()