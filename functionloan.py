#using python function and user input
#calculate the simple interest on a loan
#if the principal,rate and time are supplied through user input
def loan():
    print("insert the principal")
    p=float(input())
    print("insert the rate")
    r=float(input())
    print("insert the time")
    t=float(input())
    x=p*r*t/100
    print("this is my simple interest",x)
loan()
