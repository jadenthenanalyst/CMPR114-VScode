import random

heads = 1
tails = 2
tosses = 10

def main():
    for toss in range(tosses):
        if random.randint(heads, tails) == heads:
            print('Heads')
        if random.randint(heads, tails) == tails:
            print('Tails')

main()
