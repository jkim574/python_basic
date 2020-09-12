
def fill(state, max, which):
    # Make a copy of state
    state_copy = state[:]
    state_copy[which] = max[which]
    return state_copy

def empty(state, max, which):
    # Make a copy of state
    state_copy = state[:]
    state_copy[which] = 0
    return state_copy

def xfer(state, max, source, dest):
    # Make a copy of state
    state_copy = state[:]
    src = state_copy[source]
    dst = state_copy[dest]

    dst_remaining = max[dest] - dst
    pour_amount = min(src, dst_remaining)
    state_copy[source] -= pour_amount
    state_copy[dest] += pour_amount
    return state_copy

def succ(state, max):
    # fill() has two options: fill either left or right
    s0 = fill(state, max, 0)
    s1 = fill(state, max, 1)

    # empty() has two options: empty either left or right
    s2 = empty(state, max, 0)
    s3 = empty(state, max, 1)

    # xfer() has two options: xfer from left to right, or xfer from right to left
    s4 = xfer(state, max, 0, 1)
    s5 = xfer(state, max, 1, 0)

    # List of all possible states (which could have duplicates)
    possible_states = [s0, s1, s2, s3, s4, s5]

    # Remove duplicates
    unique_states = []
    for s_possible in possible_states:
        if not _in_unique(s_possible, unique_states):
            unique_states.append(s_possible)

    # Print unique states
    for s in unique_states:
        print(s)


# Helper function that returns True if new_item is already present in item_list, False otherwise.
def _in_unique(new_item, item_list):
    for item in item_list:
        if new_item == item:
            return True
    return False


def main():
    s0 = [0, 0]
    max = [5, 7]
    print(fill(s0, max, 1))
    print(fill(s0, max, 0))

    s1 = fill(s0, max, 1)
    print(xfer(s1, max, 1, 0))

    succ(s0, max)

    max = [5, 7]
    s0 = [3, 1]
    succ(s0, max)

    s0 = [0, 0]
    max = [3, 7]
    print(s0 == empty(s0, max, 1))


if __name__ == '__main__':
    main()
