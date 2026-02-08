def supplyradius():
    print("enter the radius")
    radius=float(input())
    return radius
def calculatecircle(radius):
    print("enter the pie")
    pie=float(input())
    area=pie*radius*radius
    print("this is the area",area)
calculatecircle(supplyradius())
