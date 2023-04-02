def str():
    string = input('Please enter a string: ')
    vowels = ["a","e","i","o","u"]

    v_count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            v_count += 1

    c_count = len(string) - v_count

    print(f'The number of vowels: {v_count}')
    print(f'The number of consonants: {c_count}')

str()