from functools import reduce
import heapq

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            x = []
            for c in line:
                if c != "\n":
                    x.append(c)
            input.append(x)

    
    return input

def expand_galaxy_map(gmap):
    expanded_map = []
    # By row
    for row in gmap:
        if all(x == "." for x in row):
            expanded_map.append(["." for _ in row])
        expanded_map.append([x for x in row])
    # By columns
    offset = 0
    for col in range(len(gmap[0])):
        if is_expandable_column(gmap, col):
            for row in expanded_map:
                row.insert(col + offset, ".")
            offset += 1
    return expanded_map

def is_expandable_column(gmap, i):
    for row in gmap:
        if row[i] != ".":
            return False
    
    return True

def get_expansions(gmap):
    expanded_rows = []
    expanded_cols = []
    # By row
    for i, row in enumerate(gmap):
        if all(x == "." for x in row):
            expanded_rows.append(i)
    # By columns
    for col in range(len(gmap[0])):
        if is_expandable_column(gmap, col):
            expanded_cols.append(col)
    return (expanded_rows, expanded_cols)

def euclidian_distance(start, end, expanded_rows=None, expanded_cols=None):
    if expanded_rows is None and expanded_cols is None:
        return abs(start[0] - end[0]) + abs(start[1] - end[1])
    
    d = abs(start[0] - end[0]) + abs(start[1] - end[1])
    rows = 0
    cols = 0
    (si, sj) = start
    (ei, ej) = end
    for r in expanded_rows:
        if si < r and ei > r:
            rows += 1
    for c in expanded_cols:
        if sj < ej:
            if sj < c and ej > c:
                cols += 1
        else:
            if sj > c and ej < c:
                cols += 1
    EMPTY_ROWS = 1000000
    return d + (rows+cols) * (EMPTY_ROWS-1)

def part1():
    gmap = read_input("1.txt")
    gmap = expand_galaxy_map(gmap)
    
    galaxy_map = {}
    galaxy_count = 0
    for i, row in enumerate(gmap):
        for j, col in enumerate(row):
            if col == "#":
                galaxy_map[galaxy_count] = (i, j)
                galaxy_count += 1
    
    sum_cost = 0
    for i in range(galaxy_count):
        start = galaxy_map[i]
        for j in range(i+1, galaxy_count, 1):
            end = galaxy_map[j]
            sum_cost += euclidian_distance(start, end)
    print(sum_cost)
    


def part2():
    gmap = read_input("1.txt")
    (expanded_rows, expanded_cols) = get_expansions(gmap)
    
    galaxy_map = {}
    galaxy_count = 0
    for i, row in enumerate(gmap):
        for j, col in enumerate(row):
            if col == "#":
                galaxy_map[galaxy_count] = (i, j)
                galaxy_count += 1
    
    sum_cost = 0
    for i in range(galaxy_count):
        start = galaxy_map[i]
        for j in range(i+1, galaxy_count, 1):
            end = galaxy_map[j]
            sum_cost += euclidian_distance(start, end, expanded_rows, expanded_cols)
    print(sum_cost)
    

    
part1()
part2()


'''
A*


# Go though all pairs and find shrotest path (only L, R, D) - A*
    sum_cost = 0
    for i in range(galaxy_count):
        start = galaxy_map_rev[i]
        # print(i)
        for j in range(i+1, galaxy_count, 1):
            # print(f" --- {j}")
            end = galaxy_map_rev[j]
            # print(f"{start} --> {end}")
            visited = [[9999999 for _ in range(len(gmap[0]))] for _ in range(len(gmap))]
            nodes = []
            heapq.heappush(nodes, (euclidian_distance(start, end), (0, start)))
            while len(nodes) > 0:
                (_, (real_cost, current_node)) = heapq.heappop(nodes)
                if current_node == end:
                    sum_cost += real_cost
                    # print(f"RC: {real_cost}")
                    break
                (ci, cj) = current_node
                if visited[ci][cj] < real_cost:
                    continue
                else:
                    visited[ci][cj] = real_cost
                if ci < len(gmap)-1:
                    next_node = (ci+1, cj)
                    heapq.heappush(nodes, (real_cost + 1 + euclidian_distance(next_node, end), (1+real_cost, next_node)))
                if cj > 0:
                    next_node = (ci, cj-1)
                    heapq.heappush(nodes, (real_cost + 1 + euclidian_distance(next_node, end), (1+real_cost, next_node)))
                if cj < len(gmap[0])-1:
                    next_node = (ci, cj+1)
                    heapq.heappush(nodes, (real_cost + 1 + euclidian_distance(next_node, end), (1+real_cost, next_node)))
    print(sum_cost)

'''