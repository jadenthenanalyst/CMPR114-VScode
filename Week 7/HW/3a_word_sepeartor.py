import re

sentence = input('Enter a sentence: ')

list = sentence.split()
list = [i.title() for i in list]

together = ''.join(list)
print(together)

res1 = [s for s in re.split('([A-Z][^A-Z]*)', together) if s]
seperator = ' '.join(res1)
print(f"{seperator}.")