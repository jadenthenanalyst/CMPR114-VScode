def write_total():
    
    outfile = open('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 7\\InClass\\total.txt', 'w')
    
    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum = 0

    for value in numbers:
        sum += value

    average = sum / len(numbers)
    outfile.write(f"The list is: {numbers}\n")
    outfile.write(f"The sum is: {sum}\n")
    outfile.write(f"The average is: {average}\n")

write_total()