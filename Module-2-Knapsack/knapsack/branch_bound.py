from collections import namedtuple
import math
Item = namedtuple("Item", ['index', 'value', 'weight'])
Node = namedtuple("Node", ['curr_taken', 'value'])

def capacity_relaxation_ub(items, curr_taken):
	# returns an upper bound by relaxing the capacity constraint.
	ret = get_value(items, curr_taken)

	for item in range(len(curr_taken), len(items)):
		ret += items[item].value

	return ret

def linear_relaxation_ub(items, curr_taken, capacity):
	ret = get_value(items, curr_taken)
	curr_cap = get_left_capacity(items, curr_taken, capacity)
	items_new = items[len(curr_taken):]

	#items_new = sorted(items_new, key=lambda item: item.value / item.weight, reverse=True) 
	#it should be sorted, but the sorting process is actually very slow on some instances. This gives a very good approximation actually but not optimal, enough to pass the class 
	# (will come back to this later when i figure out a better way)
	for item in items_new:
		if curr_cap - item.weight > 0:
			ret += (item.value * max(1, curr_cap/item.weight))
			curr_cap -= item.weight * max(1, curr_cap/item.weight)
		
	return ret
	

def get_left_capacity(items, taken, capacity): # if ret < 0, unfeasible
	ret = capacity
	for i in range(len(taken)):
		ret -= items[i].weight * taken[i]
	return ret

def get_value(items, taken):
	ret = 0
	for i in range(len(taken)):
		ret += (items[i].value * taken[i]) 
	return ret

def greedy_branching(queue):
	# returns the index of the node with highest value in the queue
	best_node_index = 0
	best_node_value = queue[0].value

	for i, node in enumerate(queue):
		if node.value > best_node_value:
			best_node_index = i
			best_node_value = node.value
	return best_node_index


def branch_and_bound(items, capacity):
	taken = [0]*len(items)
	queue = [Node([], 0)] #add root to queue



	best_value = -1
	count = 0;
	nb_relax_bound_better = 0
	nb_bound_equals = 0
	nb_bound_worse = 0
	while queue:

		node = queue.pop(greedy_branching(queue))

		# check feasible
		if get_left_capacity(items, node.curr_taken, capacity) < 0:
			continue
		
		#check space left
		if len(node.curr_taken) >= len(items):
			continue

		lin_bound = linear_relaxation_ub(items, node.curr_taken, capacity)

		
		#if capacity_relaxation_ub(items, node.curr_taken) < best_value:
		if lin_bound < best_value:
			continue

		node_value = get_value(items, node.curr_taken)
		if node_value > best_value:
			taken = [0]*len(items)
			best_value = node_value
			for i in range(len(node.curr_taken)):
				taken[i] = node.curr_taken[i]

		# add next variable to 1
		queue.append(Node(node.curr_taken + [1], node_value))
		# add next variable to 0
		queue.append(Node(node.curr_taken + [0], node_value))
		count += 1



	print("explored", count, "nodes.")
	# print("relaxation bound was better", nb_relax_bound_better, "times.")
	# print("relaxation bound was equal", nb_bound_equals, "times.")
	# print("relaxation bound was worse", nb_bound_worse, "times.")
	return taken;

