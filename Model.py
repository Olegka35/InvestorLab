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
        return '{} {:.2f} {}; cost = {}; reward = {}'\
            .format(self.title, self.price, self.count, self.cost, self.reward)


class Investor:

    def __init__(self, days, lots, money):
        self.days = days
        self.lots = lots
        self.money = money

        self.bonds_list = []
        self.reward = 0
