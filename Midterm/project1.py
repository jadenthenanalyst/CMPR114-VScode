def main():
    fat_value = float(input('Enter fat grams: '))
    carb_value = float(input('Enter carb grams: '))
    carb_calculation(carb_value)
    fat_calculation(fat_value)
    show_fat_value(fat_calorie)
    show_carb_value(carb_calorie)

def carb_calculation(carb_value):
    global carb_calorie
    carb_calorie = carb_value * 4
    return carb_calorie

def fat_calculation(fat_value):
    global fat_calorie
    fat_calorie = fat_value * 9
    return fat_calorie

def show_carb_value(carb_calorie):
    print(f"The calories from carb is: {carb_calorie:,.2f} calories")

def show_fat_value(fat_calorie):
    print(f"The calories from fat is: {fat_calorie:,.2f} calories")

main()