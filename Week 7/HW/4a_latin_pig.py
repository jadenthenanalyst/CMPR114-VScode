str = input('Enlish: ')

words = str.split()

latin_words = [i[1:] + i[0] + 'ay' for i in words]

pig = ' '.join(latin_words)
print(f"Pig Latin: {pig.upper()}")