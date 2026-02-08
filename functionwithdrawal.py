def withdrawmoney():
    print("enter the money to collect")
    money=float(input())
    return money

def purchase(money):
    yam=1000*3
    egg=24*250
    noodles=10000*2
    expense=yam+egg+noodles
    balance=money-expense
    print("this is your remaining balance",balance)
purchase(withdrawmoney())
