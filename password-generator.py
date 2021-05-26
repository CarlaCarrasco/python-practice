import random
import string

print('Welcome to the Password Generator!')

letters = input('How many letters would you like in your password?')
symbols = input('How many symbols would you like?')
numbers = input('How many numbers would you like?')
randLetters = ''
randNumbers = None

for x in range(letters):
    randLetters += random.choice(string.ascii_letters)
    print(randLetters)

for x in range(numbers):
    print(random.randint(0, 9))
