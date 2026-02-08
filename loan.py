## loan format
#Mrs ayeni balance and mr philip profit both were borrowed as loan 
# for 2 years at 5 % rate 
# find the simple interest and print it out
#in another python function
def loan():
    print("enter the principal")
    principal=float(input())
    time=2
    rate=5
    SI=principal*time*rate/100
    print(SI)
loan()