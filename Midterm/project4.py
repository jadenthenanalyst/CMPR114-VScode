def WriteInput():

    rent_expense = float(input("Please enter your RENT expense: $"))
    gas_expense = float(input("Please enter your GAS expense: $"))
    food_expense = float(input("Please enter your FOOD expense: $"))
    clothing_expense = float(input("Please enter your CLOTHING expense: $"))
    car_payment_expense = float(input("Please enter your CAR PAYMENT expense: $"))

    project4file = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Midterm\\Expenses.txt','a')

    project4file.write("Rent expenses: $" + str(rent_expense) + "\n")
    project4file.write("Gas expenses: $" + str(gas_expense) + "\n")
    project4file.write("Food expenses: $" + str(food_expense) + "\n")
    project4file.write("Clothing expenses: $" + str(clothing_expense) + "\n")
    project4file.write("Car payment expenses: $" + str(car_payment_expense) + "\n")

    print('the information have been recorded')

WriteInput()

def ReadInput():

    project4file = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Midterm\\Expenses.txt','r')

    project4content = project4file.read()

    project4file.close()

    print(project4content)

ReadInput()