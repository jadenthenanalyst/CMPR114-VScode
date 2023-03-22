salary = int(input("enter the salary: "))
num_days = int(input("enter the days of sales: "))
total = 0

for count in range(1, num_days+1):
    sales = float(input("enter the sales for day # " + str(count) + " : "))
    total += sales

if total > 1000:
    salary = (total * .1) + salary
print(f"total is: {total}")
print(f"salary is: {salary}")



