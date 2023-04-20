import class3

def main():

    start_bal = float(input("Enter the starting balance: "))

    savings = class3.BankAccount(start_bal)

    pay = float(input("How much were you paid this week? "))
    print("Will deposit that amount into your account")

    savings.deposit(pay)
    print("Your account balance is: $", format(savings.get_balance(), ',.2f'))

    cash = float(input("How much would you like to widraw? $"))
    print("Will withdrawal that amount into your account!")

    savings.withdraw(cash)

    print("Your account balance is: $", format(savings.get_balance(), ',.2f'))

main()