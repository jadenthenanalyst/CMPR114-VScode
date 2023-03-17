def main():
    hour_worked = float(input('How man hour did you work: '))
    hourly_pay = float(input('What is your hourly salary: '))
    total_salary = hour_worked * hourly_pay
    show_hour_worked(hour_worked)
    show_hourly_pay(hourly_pay)
    show_total_salary(total_salary)


def show_hour_worked(hour_worked):
    print(f'Your total hours worked is: {hour_worked:,.0f}')

def show_hourly_pay(hourly_pay):
    print(f'Your hourly salary is: ${hourly_pay:,.2f}.')

def show_total_salary(total_salary):
    print(f'Your total salary is: ${total_salary:,.2f}')

main()
