def main():

    names = ['Howard', 'Jamie', 'Jill']

    print('The list before the insert or remove: ')

    print(names)

    NameRemove = input('Enter the name to remove: ')

    names.insert(0, 'Joe')
    names.remove(NameRemove)
    print('The list after the insert: ')

    print(names)

main()

def total():
        
    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value

    average = sum / len(numbers)
    print('the total is: ', sum, '  the average is: ', average)

total()