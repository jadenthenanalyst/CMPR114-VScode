import vehicles

def main():

    used_car = vehicles.Automobiles('Audi',2022,45000,80000.0, 2)

    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print(f'Price: $ {used_car.get_price()}')
    print(f'This vehicle has {used_car.get_doors()} doors\n')


    used_car2 = vehicles.Automobiles('Honda',2011,100000,10000.0, 4)
    print('Make: ', used_car2.get_make())
    print('Model: ', used_car2.get_model())
    print('Mileage: ', used_car2.get_mileage())
    print(f'Price: $ {used_car2.get_price()}')
    print(f'This vehicle has {used_car2.get_doors()} doors\n')
 

main()