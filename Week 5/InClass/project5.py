number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

main()

def add(num1, num2):
    global total
    total = num1 + num2
    return total

add(3,4)
print(total)