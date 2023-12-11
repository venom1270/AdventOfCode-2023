def read_input(filename):
    seeds = []
    maps = []
    with open(filename, "r", encoding="utf8") as f:
        m = []
        for line in f.readlines():
            if line.startswith("seeds"):
                seeds = [int(x) for x in line.split(": ")[1].split(" ")]
            elif line == "\n":
                maps.append(m)
                m = []
            elif line[0].isnumeric():
                s = [int(x) for x in line.split(" ")]
                m.append((s[0], s[1], s[2]))
        maps.append(m)
                
    return (seeds, maps)


def part1():
    (seeds, maps) = read_input("1.txt")
    locations = []
    for seed in seeds:
        number = seed
        for map in maps:
            for m in map:
                if number >= m[1] and number <= m[1]+m[2]:
                    number = number - (m[1]-m[0])
                    break
        locations.append(number)

    print(min(locations))

def part2():
    # TODO: interval problem... optimize!!
    (seeds_temp, maps) = read_input("test.txt")
    seeds = []
    for i in range(0, len(seeds_temp), 2):
        seeds += list(range(seeds_temp[i], seeds_temp[i] + seeds_temp[i+1] + 1, 1))
    print(len(seeds))
    locations = []
    for seed in seeds:
        number = seed
        for map in maps:
            for m in map:
                if number >= m[1] and number <= m[1]+m[2]:
                    number = number - (m[1]-m[0])
                    break
        locations.append(number)

    print(min(locations))

part1()
part2()