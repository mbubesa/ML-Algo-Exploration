# Using if-elif-else statements

age = int(input('Enter your age: '))


if not (age < 0):         # Proceed as long as the age is a positive integer
    if age <= 18:   
        print('Child.')
    elif 18 < age <= 35:
        print('Youth.')
    elif 35 < age <= 150:
        print('Mature.')
    else:
        print('A PRIME')
else:
    print('Invalid age.')
