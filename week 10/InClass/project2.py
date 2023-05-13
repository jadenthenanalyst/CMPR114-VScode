import vehicles

def main():

    used_car = vehicles.Automobiles('Audi',2022,45000,80000.0)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: $', used_car.get_price())


main()