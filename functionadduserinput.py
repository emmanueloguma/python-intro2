#write a python function code that will add two numbers together
#89 and 59

def add():
    a=89
    b=59
    c=a+b
    print(c)
add()


def add2():
    print("enter the value of a")
    a=int(input())
    print("enter the value of b")
    b=int(input())
    c=a+b
    print(c)
add2()

#introducing adding values at run time
def add3(a,b):
    c=a+b
    print(c)
add3(89,59)

def add4(a,b,c):
    d=a+b+c
    print(d)
add4(89,59,69)


def multiply(a,b,c):
    d=(a*b)-c
    print(d)
multiply(89,59,69)



