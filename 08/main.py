from functools import reduce

def read_input(filename):
    input = []
    dirs = []
    nodes = []
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        dirs = lines[0].replace("\n", "")
        for line in lines[2:]:
            s = line.split(" = ")
            start = s[0]
            ends = s[1].split(", ")
            left = ends[0][1:]
            right = ends[1].replace(")", "").replace("\n", "")
            nodes.append((start, left, right))
    
    return (dirs, nodes)

def part1():
    (directions, nodes) = read_input("1.txt")

    current_node = "AAA"
    node_map = {}
    for n in nodes:
        node_map[n[0]] = (n[1], n[2])
    dir_i = 0
    num_steps = 0
    while current_node != "ZZZ":
        if directions[dir_i] == "L":
            current_node = node_map[current_node][0]
        else:
            current_node = node_map[current_node][1]
        num_steps += 1
        dir_i += 1
        if dir_i >= len(directions):
            dir_i = 0

    print(num_steps)   
   

def part2():
    (directions, nodes) = read_input("1.txt")

    current_nodes = [n for (n,_,_) in nodes if n.endswith("A")]
    print(len(current_nodes))

    # steps, dir_i, node
    memos = [{}] * len(current_nodes)
    cycle_found = [False] * len(current_nodes)

    node_map = {}
    for n in nodes:
        node_map[n[0]] = (n[1], n[2])
    dir_i = 0
    num_steps = 0
    end = False
    finals = []
    while not end:
        for i in range(len(current_nodes)):
            if not cycle_found[i]:
                if current_nodes[i].endswith("Z"):
                    key = current_nodes[i] + "#" + str(dir_i)
                    if key in memos[i]:
                        cycle_found[i] = True
                        memos[i][key] = (num_steps, memos[i][key][0], num_steps - memos[i][key][0])
                        finals.append(memos[i][key])
                        print(f"CYCLE_FOUND {i} {num_steps} {memos[i][key]}")
                        break
                    else:
                        memos[i][key] = (num_steps, 0)
                if directions[dir_i] == "L":
                    current_nodes[i] = node_map[current_nodes[i]][0]
                else:
                    current_nodes[i] = node_map[current_nodes[i]][1]
        num_steps += 1
        dir_i += 1
        if dir_i >= len(directions):
            dir_i = 0
        end = len([1 for x in current_nodes if x.endswith("Z")]) == len(current_nodes)

    print(num_steps)  

    x = 1
    y = 1
    for i in finals:
        x *= i[2]
        y *= i[0]
    print(x)
    print(y)
    print(x+y)

    x = [i[2] for i in finals]
    y = [i[0] for i in finals]

    from math import lcm
    lcmx = 1
    for i in x:
        lcmx = lcm(lcmx, i)
    lcmy = 1
    for i in y:
        lcmy = lcm(lcmy, i)
    print(lcmx)
    print(lcmy)
    print(lcmx + lcmy)

    
part1()
part2()