def sales():

    num_days = int(input("enter the days of sales: "))
    sales_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\Week 6\\InClass\\file\\sales.txt","a")

    for count in range(1, num_days+1):
        sales = float(input("enter the sales for day # " + str(count) + " : "))
        sales_file.write(str(sales) + '\n')

    sales_file.close()
    print('sales recorded')

sales()

def ReadSales():

    sales_file = open("C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\Week 6\\InClass\\file\\sales.txt","r")

    line = sales_file.readline()

    while line != "":
        amount = float(line)

        print(format(amount, ".2f"))

        line = sales_file.readline()

    sales_file.close()

ReadSales()