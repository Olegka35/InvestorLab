import sys
import random

from utils import random_word

try:
    _, name, days_num, max_lots_num, investor_sum = sys.argv
except ValueError:
    print('Incorrect parameters, use: python generate.py [file name] [days number] [max lots number] [investor sum]')
    sys.exit()

days_num = int(days_num)
max_lots_num = int(max_lots_num)
investor_sum = int(investor_sum)

if days_num < 1 or max_lots_num < 1 or investor_sum < 1:
    print('Incorrect parameters, number cannot be negative or zero')
    sys.exit()

with open(name, 'w') as file:
    file.write('{} {} {}\n'.format(days_num, max_lots_num, investor_sum))

    for i in range(days_num):
        slots_num = random.randint(1, max_lots_num)
        for k in range(slots_num):
            file.write('{} {} {:.2f} {}\n'
                       .format(i + 1, random_word(10), random.uniform(50.0, 150.0), random.randint(1, 5)))
