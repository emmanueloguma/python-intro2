def supplyradius():
    print("enter the radius")
    radius=float(input())
    return radius
def calculatecylinder(radius):
    print("enter the height")
    height=float(input())
    pie=3.142
    surfarea=(2*pie*radius*height)+(2*pie*radius*radius)
    print("this is the surfarea",surfarea)
calculatecylinder(supplyradius())
