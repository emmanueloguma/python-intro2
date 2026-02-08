# Mrs ayeni monthly budget is #300,000 from her husband.
#She bought foodstuff for 40000
#She paid her monthly rent son her shop 10000
#She paid for children lessons 35000
#She paid her house help 10000
#she was given 50,000 by her dad
#calculate how much she has left in her account in python function
def budget():
    g=300000
    f=40000
    r=10000
    l=35000
    h=10000
    d=50000
    moneyspent=f+r+l+h
    moneygained=g+d
    balance=moneygained-moneyspent
    print(balance)
budget()