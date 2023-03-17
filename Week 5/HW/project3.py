state_rate = 0.05
county_rate = 0.025

def main():
    total_sales = float(input("Please enter total sales for the month: $"))
    state_tax(total_sales)
    country_tax(total_sales)
    total_sales_tax(state, country)
    show_state_tax(state)
    show_country_tax(country)
    show_total_sales_tax(total)

def state_tax(total_sales):
    global state
    state = total_sales * state_rate
    return state

def country_tax(total_sales):
    global country
    country = total_sales * county_rate
    return country

def total_sales_tax(state, country):
    global total
    total = state + country
    return total

def show_state_tax(state):
    print(f"The amount of state sales tax is: ${state:,.2f}")

def show_country_tax(country):
    print(f"The amount of country sales tax is: ${country:,.2f}")

def show_total_sales_tax(total):
    print(f"The total sales tax is: ${total:,.2f}")

main()

