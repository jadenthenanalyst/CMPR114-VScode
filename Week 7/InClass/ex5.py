def main():
    month_of_year = ['January','February','March','April','May','June','July','August','September','October','November','December']
    monthly_rain = []

    print('Please enter monthly rain:\n')

    index = 0
    for i in month_of_year:
        rain = float(input(f"Please enter rain level for {i}: "))
        monthly_rain.insert(index,rain)
        index +=1

    total_rain = total(monthly_rain)
    average_rain = total_rain/len(monthly_rain)
    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    more_rain = max(monthly_rain)
    more_rain_index = monthly_rain.index(more_rain)

    print(f'The total rain in the year was: {total_rain}')
    print(f'The average rain in each month is: {average_rain:,.2f}')
    print(f'The month with lowest rain was {month_of_year[less_rain_index]} with {less_rain} inches of rain')
    print(f'The month with highest rain was {month_of_year[more_rain_index]} with {more_rain} inches of rain')

    write('C:\\Users\\jaden\\OneDrive\\Desktop\\Test_git\\vscode\\Week 7\\InClass\\yearly_rain.txt',monthly_rain, total_rain, month_of_year)

def total(numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum

def write(name, monthly_rain, total, month_of_year):
    index = 0
    output = open(name, 'w')
    for rain in monthly_rain:
        output.writelines(f'{month_of_year[index]}: {rain} inches\n')
        index += 1
    output.writelines(f'Total rain: {total:,.2f} inches\n')
    output.writelines(f'The average rain on this year was {total/len(month_of_year)} inches\n')
    less_rain = min(monthly_rain)
    less_rain_index = monthly_rain.index(less_rain)
    more_rain = max(monthly_rain)
    more_rain_index = monthly_rain.index(more_rain)
    output.writelines(f'The month with lowest rain was {month_of_year[less_rain_index]} with {less_rain} inches of rain')
    output.writelines((f'The month with highest rain was {month_of_year[more_rain_index]} with {more_rain} inches of rain'))

main()