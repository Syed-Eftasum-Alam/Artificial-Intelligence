import math

def init():
    return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]

def calc_cost(state):
    cost = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if (state[i] > state[j]) and (i < j):
                cost += 1
    return cost

def state_generation(current_state): 
  while True:
    current_cost = calc_cost(current_state)
    min_cost = math.inf
    min_state = None 
    for i in range(len(current_state)):
        for j in range(i+1, len(current_state)):
            new_state = current_state.copy()
            temp = new_state[i]
            new_state[i] = new_state[j]
            new_state[j] = temp
            new_cost = calc_cost(new_state)
            if new_cost < min_cost:
                min_cost = new_cost
                min_state = new_state
    if min_cost < current_cost:
        current_state = min_state
        current_cost = min_cost
    else:
        return current_state, calc_cost(current_state)


def main():
    print("Hill Climbing Algorithm")
    state = init()
    print (state_generation(state))
    
main()