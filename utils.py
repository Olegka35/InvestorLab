import random
import string

from Model import Investor, Bond


def read_input_file(input_file_path):
    with open(input_file_path) as input_file:
        days_num, lots_num, money = input_file.readline().split()
        investor = Investor(int(days_num), int(lots_num), int(money))
        bonds = []
        for line in input_file:
            launch_day, title, price, count = line.split()
            bonds.append(Bond(int(days_num) - int(launch_day), str(title), float(price), int(count)))
        return investor, bonds


def dynamic_programming_solution(investor, bonds):
    investor_money = investor.money
    mem_table = [[0 for _ in range(investor_money + 1)] for _ in range(len(bonds) + 1)]

    for i in range(len(bonds) + 1):
        for j in range(investor_money + 1):
            if i == 0 or j == 0:
                mem_table[i][j] = 0

            elif bonds[i - 1].cost <= j:
                mem_table[i][j] = max(bonds[i - 1].reward + mem_table[i - 1][j - bonds[i - 1].cost], mem_table[i - 1][j])

            else:
                mem_table[i][j] = mem_table[i - 1][j]

    n = len(bonds)
    res = mem_table[n][investor_money]
    available_money = investor_money

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == mem_table[i - 1][available_money]:
            continue
        else:
            investor.bonds_list.append(bonds[i - 1])
            investor.reward += bonds[i - 1].reward
            res -= bonds[i - 1].reward
            available_money -= bonds[i - 1].cost

    return investor.bonds_list


def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def write_output_file(output_path, investor):
    with open(output_path, 'w') as file:
        file.write('{}\n'.format(investor.reward))

        for bond in investor.bonds_list:
            file.write('{} {} {:.1f} {}\n'.format(investor.days - bond.days, bond.title, bond.price, bond.count))