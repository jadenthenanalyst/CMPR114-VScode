import random

first_names=('John','Andy','Joe','Donald','Michael')
last_names=('Johnson','Smith','Williams','Huynh','Nguyen')
names = []
group="".join(random.choice(first_names)+" "+random.choice(last_names) + "\n" for _ in range(5))
print("Here are 5 random generated name: ")
print(group)
