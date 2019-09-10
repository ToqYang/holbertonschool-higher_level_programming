#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_Number = number % -10
elif number > 0:
    last_Number = number % 10
print("Last digit of {:d}".format(number), end=' ')
print("is {:d}".format(last_Number), end=' ')
if last_Number == 0:
    print("and is 0")
elif last_Number > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
