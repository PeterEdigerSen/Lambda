import tkinter as tk

# lambda function definition
#  lambda::=
#  lambda <par1>,<par2>,... : <expression>
print('\n      Constants, variables, functions')
5
v = 5
v


def f():
    print('Yeye')


f
f()

print('\n      Simple lambda example:')
div = lambda a, b: a / b
print(div(2, 3))

print('\n      The same with a usual function:')


def div_classic(a, b):
    return a / b


print(div_classic(2, 3))

print('\n      What is the type of lambda function?')
print(div)
print(type(div))

# Seems to be approximately the same

print('\n      Lambda can be used as variable:')
mult = lambda a, b: a * b


def operate(operation):
    print(operation(2, 3))


operate(div)
operate(mult)

print('\n      Another example. We define a generic divider, and use it to produce special dividers')


def generic_divider(b):
    return lambda a: a / b


take_a_half = generic_divider(2)
take_a_third = generic_divider(3)
take_one_percent = generic_divider(100)
print(take_a_half(10))
print(take_a_third(10))
print(take_one_percent(10))

# Restriction for lambda: it is only one expression



