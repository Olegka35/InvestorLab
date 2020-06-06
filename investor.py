import sys
import time

from utils import read_input_file, dynamic_programming_solution, write_output_file, numba_solution

try:
    _, alg, input_file_path, output_file_path = sys.argv

    if alg not in ('standart', 'numba'):
        raise ValueError
except ValueError:
    print('Incorrect parameters, use: [algorithm (standart / numba)] [input file] [output file]')
    sys.exit()

start_time = time.time()

investor, bonds = read_input_file(input_file_path, alg)
if alg == 'standart':
    bonds_list = dynamic_programming_solution(investor, bonds)
elif alg == 'numba':
    bonds_list = numba_solution(investor, bonds)
else:
    raise ValueError
write_output_file(output_file_path, investor, bonds_list)

duration = time.time() - start_time
print('Duration is {:.2f} ms'.format(duration * 1000))
