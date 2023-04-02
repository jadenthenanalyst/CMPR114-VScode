str = input('Enter a string: ')

str = "".join(str.split())

dict = {}

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

highest = max(dict, key=dict.get)
print(f"The most frequent character is '{highest}' with the freqency of {dict[highest]}")

