def main():
    loan_payment = float(input('Enter monthly loan payment cost: '))
    insurance = float(input('Enter monthly insurance cost: '))
    gas = float(input('Enter monthly gas cost: '))
    oil = float(input('Enter monthly oil cost: '))
    tires = float(input('Enter monthly tires cost: '))
    maintenance = float(input('Enter monthly maintenance cost: '))
    total_montly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    annual_cost = total_montly_cost * 12
    show_monthly_cost(total_montly_cost)
    show_annual_cost(annual_cost)

def show_monthly_cost(total_montly_cost):
    print(f"The monthly cost for this automobile is: ${total_montly_cost:,.2f}")

def show_annual_cost(annual_cost):
    print(f"The annual cost for this automobile is: ${annual_cost:,.2f}")

main()