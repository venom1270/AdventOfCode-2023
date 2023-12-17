from functools import reduce

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            s = line.split(" ")
            input.append((s[0], int(s[1].replace("\n", ""))))
    
    return input

def part1():
    input = read_input("1.txt")
    types = []
    for i in input:
        hand = i[0]
        bid = i[1]
        typ = 0
        value_map = {}
        for v in hand:
            if v in value_map:
                value_map[v] += 1
            else:
                value_map[v] = 1
        values = list(value_map.values())
        if 5 in values:
            typ = 0
        elif 4 in values:
            typ = 1
        elif 3 in values and 2 in values:
            typ = 2
        elif 3 in values:
            typ = 3
        elif values.count(2) == 2:
            typ = 4
        elif 2 in values:
            typ = 5
        else:
            typ = 6
        types.append((hand, bid, typ))

    def compare(x, y):
        h1 = x[0]
        t1 = x[2]
        h2 = y[0]
        t2 = y[2]
        if t1 < t2:
            return 1
        elif t2 < t1:
            return -1
        else:
            m = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
            for i in range(len(h1)):
                c1 = int(m.get(h1[i], h1[i]))
                c2 = int(m.get(h2[i], h2[i]))
                if c1 > c2:
                    return 1
                elif c2 > c1:
                    return -1
            return 0

    from functools import cmp_to_key     
    types = sorted(types, key=cmp_to_key(compare))

    #print(types)
    total_winnings = sum([x[1]*(i+1) for i, x in enumerate(types)])
    print(total_winnings)

    
   

def part2():
    input = read_input("1.txt")
    types = []
    for i in input:
        hand = i[0]
        bid = i[1]
        typ = 0
        value_map = {}
        num_jokers = 0
        for v in hand:
            if v == "J":
                num_jokers += 1
            elif v in value_map:
                value_map[v] += 1
            else:
                value_map[v] = 1
        
        if num_jokers == 5:
            value_map["K"] = 5
        else:
            max_val = max(value_map.values())
            for v in ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
                if value_map.get(v, 0) == max_val:
                    value_map[v] += num_jokers
                    break
        values = list(value_map.values())
        if 5 in values:
            typ = 0
        elif 4 in values:
            typ = 1
        elif 3 in values and 2 in values:
            typ = 2
        elif 3 in values:
            typ = 3
        elif values.count(2) == 2:
            typ = 4
        elif 2 in values:
            typ = 5
        else:
            typ = 6
        types.append((hand, bid, typ))

    def compare(x, y):
        h1 = x[0]
        t1 = x[2]
        h2 = y[0]
        t2 = y[2]
        if t1 < t2:
            return 1
        elif t2 < t1:
            return -1
        else:
            m = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10}
            for i in range(len(h1)):
                c1 = int(m.get(h1[i], h1[i]))
                c2 = int(m.get(h2[i], h2[i]))
                if c1 > c2:
                    return 1
                elif c2 > c1:
                    return -1
            return 0

    from functools import cmp_to_key     
    types = sorted(types, key=cmp_to_key(compare))

    #print(types)
    total_winnings = sum([x[1]*(i+1) for i, x in enumerate(types)])
    print(total_winnings)


    



part1()
part2()