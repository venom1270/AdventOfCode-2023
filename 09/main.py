from functools import reduce

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            s = line.split(" ")
            input.append([int(x) for x in s])
    
    return input

def part1():
    inputs = read_input("1.txt")
    history_values = []

    for history in inputs:
        history_value = history[-1]
        current_history = history
        while not all(v == 0 for v in current_history):
            next_history = []
            for i in range(len(current_history)-1):
                next_history.append(current_history[i+1] - current_history[i])
            history_value += next_history[-1]
            current_history = next_history
        history_values.append(history_value)

    print(sum(history_values))


    
   

def part2():
    inputs = read_input("1.txt")
    history_values = []

    for history in inputs:
        history_value_trace = [history[0]]
        current_history = history
        while not all(v == 0 for v in current_history):
            next_history = []
            for i in range(len(current_history)-1):
                next_history.append(current_history[i+1] - current_history[i])
            history_value_trace.append(next_history[0])
            current_history = next_history

        history_value = history_value_trace[-1]
        for i in reversed(history_value_trace[:-1]):
            history_value = i - history_value

        history_values.append(history_value)

    # print(history_values)
    print(sum(history_values))
    

    
part1()
part2()