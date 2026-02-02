#The radius of circle is 5cm, if pie =3.142. 
# Write a python code that will calculate the 
# double the area of the circle and the one third of the 
# circumference of the circle. 
# Add the two results together and print tit out

def calculatecircle():
    r=5
    pie=3.142
    area=pie*r*r
    dc=area*2
    print(dc)
    cirf=2*pie*r
    onethirdcirf=1/3*dc
    print(onethirdcirf)
    new=onethirdcirf+dc
    print(new)
calculatecircle()    