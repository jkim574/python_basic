# returns a copy of state which fills the jug corresponding to the index in which (0 or 1) to its maximum capacity
def fill(state, maxCap, which):

	# copy of state
	state_copy = state[:] 
	state_copy[which] = maxCap[which]
	return state_copy
		
# returns a copy of state which empties the jug corresponding to the index in which (0 or 1). 
def empty(state, maxCap, which):

	# copy of state
	state_copy = state[:]
	state_copy[which] = 0	
	return state_copy

# returns a copy of state which pours the contents of the jug at index source into the jug at index dest, until source is empty or dest is full.
def xfer(state, maxCap, source, dest):

	# copy of state
	state_copy = state[:]

	# source is 0 and dest is 1
	if source == 0 and dest == 1:
		
		# if the contents of the 'dest' jug overflow afte the pour
		if state_copy[source] + state_copy[dest] >= maxCap[dest]:
			subtract = maxCap[dest] - state_copy[dest]
			state_copy[source] -= subtract
			state_copy[dest] = maxCap[dest]

		# if the contents of the 'dest' jug don't overflow after the pour
		else:
			state_copy[dest] += state_copy[source]
			state_copy[source] = 0

	# source is 1 and dest is 0	
	elif source == 1 and dest == 0:
	
		#if the contents of the 'source' jug overflow after the pour	
		if state_copy[source] + state_copy[dest] >= maxCap[dest]:
			subtract = maxCap[dest] - state_copy[dest]
			state_copy[source] -= subtract	
			state_copy[dest] = maxCap[dest]

		#if the contents of the 'source' jug don't overflow after the pour
		else:
			state_copy[dest] += state_copy[source]
			state_copy[source] = 0

	return state_copy 


# prints the list of unique successor states of the current state in any order. 
def succ(state, maxCap):
	fill0 = fill(state, maxCap, 0)	
	fill1 = fill(state, maxCap, 1)
	empty0 = empty(state, maxCap, 0)
	empty1 = empty(state, maxCap, 1)
	xfer01 = xfer(state, maxCap, 0, 1)
	xfer10 = xfer(state, maxCap, 1, 0) 

	add = [fill0, fill1, empty0, empty1, xfer01, xfer10]
	result = []

	# Convert items to a tuple, then convert it the whole thing to a set, then convert everything back to a list:
	result = list(set(tuple(item) for item in add))
	
	# Convert to list of list
	result = list(list(item) for item in result)
	print(result)

"""
# main	
if __name__ == "__main__":
	s0 = [0, 0]
	max = [1, 2]	 
	succ(s0, max);
"""
