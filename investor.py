import sys

from utils import read_input_file, dynamic_programming_solution, write_output_file

try:
    _, input_file_path, output_file_path = sys.argv
except ValueError:
    print('Incorrect parameters, use: [input file] [output file]')
    sys.exit()


investor, bonds = read_input_file(input_file_path)

dynamic_programming_solution(investor, bonds)

write_output_file(output_file_path, investor)

