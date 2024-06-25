from util import *

n1 =  6
n2 = 13

result1 = to_square(n1)
result2 = to_square(n2)

print("Hello world... :)")
print("Result 1", result1)
print("Result 2: ",result2)

print(123 + 222)
print(1.5 * 4)
print(2 ** 100)

print(3.1415 * 2)

import math

print(math.pi)


import random
print(random.random())
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 20]))


##################### Strings ######################33
s = 'ABCDEFGH'
print(len(s))
print(type(s))
print(s[0])
print("For loop")
for i in range(0, len(s)):
    print(-i+len(s)-1, s[-i+len(s)-1])

print("End of FOR loop")
print('*' * 10)
print(s[:])     # ABCDEFGH
print(s[1:])    # BCDEFGH
print(s[1:3])   # BC
print(s[1:2])   # B
print(s[:3])    # ABC
print(s[0:3])   # ABC
print(s[:-1])   # ABCDEFG
print(s[:-2])   # ABCDEF
print(s[:-3])   # ABCDE


print(s[0:6:2]) # ACE

print(s[::-1]) # Reverse String

print(s[6:2:-1]) # Slicing in the reverse order

print(s + 'XYZ') # Concatenation
print(s)  # ABCDEFGH => No change in s string
print(s * 8)  # This is not an integer multiplication. But is repeates the string

print(s[0])

# s[0] = 'X'  # Gives error
# THe string index value can not be changed. This is called Immutability

s = 'X' + s[1:]  # String Concatenation + String Slicing
print(s[0])
print(s)

## String Methods


print("String Methods" + ' *' * 10)

string1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string1)
string2 = string1.replace('ABC','XYZ')
print(string2)
print(string2.find('XYZ'))
print(string2.lower())

string3 = "HI Krisha, you have missed 'split' function"

print(string3)

print(string3.split(','))

print(string3.split("'"))

string4 = "ABCDPYAILABSEFGHIJKLPYAILABSMNOPQRSPYAILABSTUVWXYZPYAILABSABDEF"

print(string4)
print(string4.split('PYAILABS'))
print("String Methods" + ' *' * 10)

list4 = string4.split('PYAILABS')
print(list4)
print('---'.join(list4))

print(string4.endswith('F'))
print(string4.endswith('XYZ'))
print(string4.endswith('AILABSABDEF'))
print(string4.startswith('ABC'))

L = list(s)
print(L)
print(''.join(L))

print("String Formating expressions" + 10 * ' * ')

print("There are %d - %s (s) are present." %(10, 'BOOK'))

print("We need to buy %d %s (s) and each costs %g$" %(10, 'Book', 55.50))

print("We need to buy %s %s (s) and each costs %ss" %(10, 'Book', 55.50))

print('%s --- %s --- %s' %(42, 3.14, [1, 2, 8, 10]))