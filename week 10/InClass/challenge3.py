import vehicles

def main():

    used_car = vehicles.Automobiles('Audi',2022,45000,80000.0)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print(f'Price: $ {used_car.get_price()} \n')

    used_car2 = vehicles.Automobiles('Honda',2011,100000,10000.0)
    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print(f'Price: $ {used_car2.get_price()} \n')
 

main()