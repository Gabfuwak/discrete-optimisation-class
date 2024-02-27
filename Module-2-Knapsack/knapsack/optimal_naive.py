from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def optimal_naive(items, capacity):
    # A naive full search to fill a knapsack with the best combination possible
    # Tries all possible solutions so it is very slow
    best_knapsack = []
    best_val = 0
    count = 0

    for item in items:
        count += 1
        new_capacity = capacity - item.weight
        new_items = items[:]
        new_items.pop(count-1)

        candidate_value = 0
        candidate = []

        if new_capacity >= 0:
            candidate_value = item.value 
            candidate = [item]
            candidate += optimal_naive(new_items, new_capacity)
            
            for candidate_item in candidate:
                candidate_value += candidate_item.value

        if candidate_value > best_val:
            best_val = candidate_value
            best_knapsack = candidate

    return best_knapsack