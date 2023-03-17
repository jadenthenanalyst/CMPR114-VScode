def main():
   
    firstname = input('Enter your first name: ')

    lastname = input('Enter your last name: ')

    adress = input('Enter your street adress: ')

    city = input('Enter your city: ')

    state = input('Enter your state: ')

    zip = input('Enter your zip code: ')

    full_name(firstname, lastname)
    full_adress(adress, city, state, zip)

def full_name(firstname, lastname):
    print(f'Your full name is: {firstname} {lastname} ')

def full_adress(adress, city, state, zip):
    print(f'Your address is: {adress} {city}, {state} {zip} ')

main()
