def sales():

    total = 0
    salary = int(input("enter your salary: "))
    num_days = int(input("enter the days of sales: "))

    sales_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\Week 6\\InClass\\file\\sales.txt","a")

    for count in range(1, num_days+1):

        sales = float(input("enter the sales for day # " + str(count) + " : "))
        total += sales
        sales_file.write("sales for day # " + str(count) + " is: " +str(sales) + "\n")

    if total > 1000:
        salary = (total * .1) + salary
        sales_file.write("New salary with bonus is: " + str(salary) + "\n")
    sales_file.close()
    print('sales recorded')

sales()

def ReadSales():

    sales_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\Week 6\\InClass\\file\\sales.txt","r")

    line = sales_file.readline()

    while line != "":
        amount = line

        print(amount)

        line = sales_file.readline()

    sales_file.close()

ReadSales()