def main():

    while True:

        try:

            hours = int(input("hours worked: "))

            pay = float(input("hourly pay: "))

            gross = hours * pay

            print("gross pay $", format(gross, ",.2f"))
            break

            print("recorded")

        except ValueError:
            print('ERROR: hours worked and pay must be a valid numbers, try again ')

        except Exception as err:
            print(err)

main()