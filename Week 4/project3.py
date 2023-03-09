test_tup = ([ 17, 28],[ 93, 11],[ 20, 17])
sum = 0
for i in test_tup:
    for l in i:
        sum += l
print(f"sum of test_tup is: {sum}")
