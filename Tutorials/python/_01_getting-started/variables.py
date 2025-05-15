# Using variables

name = 'Monty'
age = 75

# using string concatenation
message1 = 'My name is ' + name + '. I am ' + str(age) + ' years old.' 

# using .format
message2 = 'My name is {}. I am {} years old.'.format(name, age)

# using a formated string (f-string)
message3 = f'My name is {name}. I am {age} years old.'

current_year = 2025

message4 = f'I was born in {current_year - age}.'

# print to standard output
print(message1)
print(message2)
print(message3)
print(message4)

