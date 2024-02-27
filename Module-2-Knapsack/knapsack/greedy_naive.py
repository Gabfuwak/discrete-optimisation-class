from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def greedy_naive(items, capacity):
    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = []

    for item in items:
        if weight + item.weight <= capacity:
            taken.append(item)
            value += item.value
            weight += item.weight

    return taken