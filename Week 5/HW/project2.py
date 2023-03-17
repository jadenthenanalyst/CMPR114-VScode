a_cost = 20
b_cost = 15
c_cost = 10

def main():
    a_seats = int(input('How many class A seats were sold: '))
    b_seats = int(input('How many class B seats were sold: '))
    c_seats = int(input('How many class C seats were sold: '))
    profit_a(a_seats)
    profit_b(b_seats)
    profit_c(c_seats)
    total_profit(a_profit,b_profit,c_profit)
    show_total_profit(sum_profit)

def profit_a(a_seats):
    global a_profit
    a_profit = a_cost * a_seats
    return a_profit

def profit_b(b_seats):
    global b_profit
    b_profit = b_cost * b_seats
    return b_profit

def profit_c(c_seats):
    global c_profit
    c_profit = c_cost * c_seats
    return c_profit

def total_profit(a_profit,b_profit,c_profit):
    global sum_profit
    sum_profit = a_profit + b_profit + c_profit
    return sum_profit

def show_total_profit(sum_profit):
    print(f"The total profit is: ${sum_profit:,.2f}")

main()
print(f"The total A profit is: ${a_profit:,.2f}")
print(f"The total B profit is: ${b_profit:,.2f}")
print(f"The total C profit is: ${c_profit:,.2f}")

