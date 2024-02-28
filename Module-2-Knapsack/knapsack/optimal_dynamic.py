from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def optimal_dynamic(items, capacity):
	# This function gives the wrong value (close approcimate but not quite the right value)
    memo_table = {}

    def hash_knapsack(knapsack):
        ret = ""
        temp = []
        for item in knapsack:
            temp.append(item.index)

        temp.sort() # we sort to get rid of symetries

        for item in knapsack: # nothing was done for hash collisions, hopefully not too much will happen
            index = temp.index(item.index) # maybe slow
            ret += str(index)
            ret += str(item.value)
            ret += str(item.weight)

        return ret

    def recursive_dynamic(items, capacity):
        # Copy paste of the naive recursive function with a check in the memo table
        hash = hash_knapsack(items)
        if hash in memo_table.keys():
            return memo_table[hash]


        best_knapsack = []
        best_val = 0
        best_cap = capacity
        count = 0

        for item in items:
            new_capacity = capacity - item.weight
            new_items = items[:]
            new_items.pop(count)

            candidate_value = 0
            candidate = []

            if new_capacity >= 0:
                candidate_value = item.value 
                candidate = [item]
                candidate += recursive_dynamic(new_items, new_capacity)
                
                for candidate_item in candidate:
                    candidate_value += candidate_item.value

            if candidate_value > best_val:
                best_val = candidate_value
                best_knapsack = candidate
                best_capacity = sum([item.weight for item in best_knapsack])
                
            count +=1

        memo_table[hash] = best_knapsack
        return best_knapsack

    return recursive_dynamic(items, capacity)
    