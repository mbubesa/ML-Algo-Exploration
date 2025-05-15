# Operators and operator precedence

# Arithmetic precedence rules - PEMDAS

# Without using parenthesis
expression_1 = 1 + 3 / 5 * 7 ** 2 - 10

# Using parenthesis
expression_2 = (1 + ((3 / 5) * (7 ** 2))) - 10

# Customizing output needs using parenthesis
salary = 7_000_000 # optional: use underscores '_' to separate digits, the output is not affected
tax = 0.2
bills = 0.1
savings = 0.3
expression_3 = salary - ((salary*tax) + (salary*bills) + (salary*savings))

# Results 1
print(f"Expression 1 solution: {expression_1}")
print(f"Expression 2 solution: {expression_2}")
print(f"Is expression 1 equivalent to expression 2: {expression_1 == expression_2}")
print(f"Is expression 1 the same as expression 2: {expression_1 is expression_2}")
print(f"Expression 3 custom solution: {expression_3}")

print('-----------------------------------')

# Boolean operations
# For and - both expressions are evaluated.
# For or - either one or both are evaluated, if the first one is True, the second is not evaluated.

expression_4 = ((3 * 2) == 6) and ((8 - 2) == 6)

# the second boolean expression is not evaluated, otherwise it would have thrown a ZeroDivisorError
expression_5 = ((5 - 5) == 0) or ((5 / 0) == 0)


# Results 2
print(f"Expression 4 solution: {expression_4}")
print(f"Expression 5 solution: {expression_5}")
