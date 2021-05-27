import random
import string

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
randLetters = ''
randNumbers = ''
randSymbols = ''

print('Welcome to the Password Generator!')

numLetters = input('How many letters would you like in your password?')
numSymbols = input('How many symbols would you like?')
numbers = input('How many numbers would you like?')


def shuffle_string():
    s = randLetters + randNumbers + randSymbols
    shuffleString = ''.join(random.sample(s, len(s)))
    print(shuffleString)


for x in range(numLetters):
    randLetters += random.choice(string.ascii_letters)
print(randLetters)


for x in range(numSymbols):
    randSymbols += random.choice(symbols)
print(randSymbols)


for x in range(numbers):
    randNumbers += str(random.randint(0, 9))
print(randNumbers)


shuffle_string()
