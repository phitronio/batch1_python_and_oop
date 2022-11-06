'''
 A B C

 A B C
 A C B
 B A C
 B C A
 C A B
 C B A   
'''
'''
DAC DUB LON IST PAR NYC KAT
'''

from itertools import permutations
# list = [1, 2, 3, 4, 5]
list = ['I', 'learn', 'python']

for i in permutations(list):
    print(i)