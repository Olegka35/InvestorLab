import numba as nb
from numba import int32, float32
from numba.experimental import jitclass


class Bond:

    value = 1000
    pay_day = 30

    def __init__(self, days, title, price, count):
        self.days = days
        self.title = title
        self.price = price
        self.count = count

        self.cost = int(Bond.value * price / 100 * count)
        self.reward = Bond.value * count + (days + Bond.pay_day) * count - self.cost

    def __repr__(self):
        return '{} {:.1f} {}; cost = {}; reward = {}'\
            .format(self.title, self.price, self.count, self.cost, self.reward)


class Investor:

    def __init__(self, days, lots, money):
        self.days = days
        self.lots = lots
        self.money = money

        self.reward = 0


@jitclass([('days', int32), ('price', float32), ('count', int32), ('cost', int32), ('reward', int32), ('title', nb.types.string)])
class NumbaBond:

    def __init__(self, days, title, price, count):
        self.days = days
        self.title = title
        self.price = price
        self.count = count

        self.cost = int(1000 * price / 100 * count)
        self.reward = 1000 * count + (days + 30) * count - self.cost

    def __repr__(self):
        return '{} {:.1f} {}; cost = {}; reward = {}'\
            .format(self.title, self.price, self.count, self.cost, self.reward)


@jitclass([('days', int32), ('lots', int32), ('money', int32), ('reward', int32)])
class NumbaInvestor:

    def __init__(self, days, lots, money):
        self.days = days
        self.lots = lots
        self.money = money

        self.reward = 0