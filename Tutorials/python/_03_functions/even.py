# even number

def is_even(number: int):
    return abs(number) % 2 == 0

counter = 0
for number in range(1452):
    if is_even(number):
        counter += 1

print("{} even numbers found.".format(counter))