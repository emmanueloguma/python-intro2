#write a python function code that will add any three numbers
#given through user input.

def bingo():
    bingo="bingo! it is greater than 1000"
    print(bingo)

def ohno():
    ohno="oh no! it is less than 1000"
    print(ohno)

def add():
    print("insert your first number")
    n1=float(input())
    print("insert your second number")
    n2=float(input())
    print("insert your third number")
    n3=float(input())
    x=n1+n2+n3
    #print(x)
    y=n1*n2*n3
    #print(y)
    new=x+y
    if new > 1000:
        bingo()
    else:
        ohno()
add()