def main():

    food = ['Pizza', 'Burger', 'Chips']

    print('here are the food items in the list')

    print(food)

    item = input('Which item in the list do you want to change?')

    try: 
        itemIndex = food.index(item)

        newItem = input('Enter the new value: ')

        food[itemIndex] = newItem

        print(' here is the revised list ')

        print(food)

    except ValueError:
        print('the item was not found in the list')

main()