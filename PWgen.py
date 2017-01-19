import random
import collections
import string

from random import shuffle
from random import randint
from collections import OrderedDict

lower = string.ascii_uppercase
upper = string.ascii_lowercase
numbers = ('1','2','3','4','5','6','7','8','9','0')
symbolq = []

maxsymbols = 10
while len(symbolq) < maxsymbols:
    query = input('Enter the symbols you wish to use (type to stop): ')
    symbolq.append(query)
    print(symbolq)
    orderedsymbolq = list(OrderedDict.fromkeys(symbolq)) #removes duplicates if inputted

orderedsymbolq = ''.join(list(orderedsymbolq))
print('Your selected symbols are:', orderedsymbolq) #orderedsymbolq is the final list of symbols to be used in password

def strong_password():
    spl = randint(0,15)
    spu = randint(0,15)
    spn = randint(0,9)
    lower1 = random.sample(lower, spl)
    upper1 = random.sample(upper, spu)
    symbols1 = orderedsymbolq
    numbers1 = random.sample(numbers, spn)
    password1 = (lower1 + upper1 + symbols1 + numbers1)
    if len(password1)>25:
        for i in range(4):
            shuffle(password1)
    elif len(password1)<25:
        for i in range(3):
            shuffle(password1)
    password1 = ''.join(list(password1))
    print(password1)

strong_password() 
    
