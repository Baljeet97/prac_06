CURRENT_YEAR = 2018
VINTAGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.year)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        if self.get_age() >= VINTAGE:
            return True
        else:
            return False


# def testing():
#     name = "Gibson L-5 CES"
#     year = 1922
#     cost = 16035.40
#
#     guitar = Guitar(name, year, cost)
#     new = Guitar("Another Guitar", 2012, 1512.9)
#
#     print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95,
#                                                       guitar.get_age()))
#     print("{} get_age() - Expected {}. Got {}".format(new.name, 5,
#                                                       new.get_age()))
#     print()
#     print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
#                                                          True,
#                                                          guitar.is_vintage()))
#     print("{} is_vintage() - Expected {}. Got {}".format(new.name,
#                                                          False,
#                                                          new.is_vintage()))
#
#
# if __name__ == '__main__':
#     testing()
