def main():
    global num1
    num1 = int(input('Enter first number: '))
    global num2
    num2 = int(input('Enter second number: '))
    global num3
    num3 = int(input('Enter third number: '))
    sum(num1, num2, num3)
    avg(total)
    show_num1()
    show_num2()
    show_num3()
 
def sum(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total

def avg(total):
    global average
    average = total / 3
    return average

def show_num1():
    print(f'The first number you entered is {num1}.')

def show_num2():
    print(f'The second number you entered is {num2}.')

def show_num3():
    print(f'The third number you entered is {num3}.')


main()
print(f'The sum of 3 numbers is: {total}')
print(f'The average of 3 numbers is: {average}')

