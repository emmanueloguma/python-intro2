def loanprincipal():
    print("enter principal for the loan to collect")
    principal=float(input())
    return principal

def calculateSI(principal):
    print("enter the rate")
    rate=float(input())
    print("enter the time")
    time=float(input())
    SI=principal*rate*time/100
    print("this is the simple interest",SI)
calculateSI(loanprincipal())