def acccount():
    print("계좌 생성")


def deposit(balance, money):   #입금
    print("입금 완료. 잔액 {0}원".format(balance+money))
    return balance+money



def withdraw(balance,money):  #출금
    if balance >=money:
        print("출금 완료, 잔액 : {0}원".format(balance-money))
        return balance-money
    else:
        print("출금 불가, 잔액 : {0}".format(balance))
        return balance


def withdraw_night(balance,money):
    commission = 100  #수수료 100원
    return commission,balance-money-commission


balance = 0

balance = deposit(balance,1000)
balance = withdraw(balance,200)
commission, balance = withdraw_night(balance,500)
print("수수료 {0}원, 잔액 {1}원".format(commission,balance))
