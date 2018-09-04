from prac_06.guitar import Guitar


def testing():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    new = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(new.name, 5,
                                                      new.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(new.name,
                                                         False,
                                                         new.is_vintage()))


if __name__ == '__main__':
    testing()
