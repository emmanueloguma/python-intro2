def add():
    oranges=40*50
    eggs=24*200
    yams=20*1500
    total=oranges+eggs+yams
    print("this is my total",total)
add()

def calculaterectangle():
    l=10
    b=5
    area=1*b
    #print(area)
    perimeter=(l+b)*2
    #print(perimeter)
    new=area+perimeter
    print(new)
calculaterectangle()

def calculatecircle():
    r=5
    pie=3.142
    area=pie*r*r
    #print(area)
    circ=2*pie*r
    #print(circ)
    new=area+circ
    print(new)
    if new ==100:
        print("hurray! yes it is equals to 100")
        x=new*5000
        print(x)
    else:
        print("oh no it is not equals to 100")
        x=new*3
        print(x)

calculatecircle()