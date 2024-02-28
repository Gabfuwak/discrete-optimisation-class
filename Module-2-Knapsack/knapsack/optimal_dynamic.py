from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def optimal_dynamic(items, capacity):
    nb_items = len(items)

    # row = items
    # column = capacity.
    memo = [[0 for _ in range(capacity+1)] for _ in range(nb_items+1)]
    #memo = np.zeros((nb_items +1, capacity+1), dtype = int)

    # Populate the table
    for cap in range(1, capacity+1):
        for item in range(1, nb_items+1):
            if items[item-1].weight <= cap:
                memo[item][cap]  = max(memo[item-1][cap], items[item-1].value + memo[item-1][cap - items[item-1].weight])
            else:
                memo[item][cap] = memo[item-1][cap]

    # Trace back
    taken = [0] * nb_items
    curr_cap = capacity-1
    for item in range(nb_items-1, -1, -1):
        if memo[item+1][curr_cap+1] != memo[item][curr_cap+1]:
            taken[item] = 1
            curr_cap -= items[item].weight


    return taken


    

    
    