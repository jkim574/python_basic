# returns a copy of state which fills the jug corresponding to the index in which (0 or 1) to its maximum capacity
def fill(state, maxCap, which):

	# copy of state
	origin = list(state)	
	
	result = origin 
	result[which] = maxCap[which]
	return result
		
# returns a copy of state which empties the jug corresponding to the index in which (0 or 1). 
def empty(state, maxCap, which):

	# copy of state
	origin2 = list(state)
	result2 = origin2
	result2[which] = 0
	return result2


# returns a copy of state which pours the contents of the jug at index source into the jug at index dest, until source is empty or dest is full.
def xfer(state, maxCap, source, dest):

	# copy of state
	origin3 = list(state)
	result3 = origin3

	# source is 0 and dest is 1
	if source < dest:
		if result3[source] + result3[dest] >= maxCap[dest]:
			sub = maxCap[dest] - result3[dest]
			result3[source] -= sub
			result3[dest] = maxCap[dest]
		else:
			result3[dest] += result3[source]
			result3[source] = 0
	# source is 1 and dest is 0	
	if source > dest:	
		if result3[source] + result3[dest] >= maxCap[dest]:
			sub = maxCap[dest] - result3[dest]
			result3[source] -= sub	
			result3[dest] = maxCap[dest]

		else:
			result3[dest] += result3[source]
			result3[source] = 0

	return result3


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
	print(result) 



# main	
if __name__ == "__main__":
	s0 = [0,0]
	max = [14,7]
	 
#	print(fill(s0, max, 1))
#	print(empty(s0, max, 0 ))
#	print(s0)
#	print(max)
#	xfer(s0, max, 1, 0)
	succ(s0, max)	
