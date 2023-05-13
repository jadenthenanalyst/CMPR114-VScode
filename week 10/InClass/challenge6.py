import vehicles2

def main():

    electric_car = vehicles2.Electric('Tesla','Y',5000,40000.0)

    print('The following Electric car is in inventory')
    print('Make: ', electric_car.get_make())
    print('Model: ', electric_car.get_model())
    print('Mileage: ', electric_car.get_mileage())
    print('Price: $', electric_car.get_price())

    print('\n')

main()