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
    (seeds, maps) = read_input("1.txt")
    print(len(seeds))
    locations = []
    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_end = seed_start + seeds[i+1]-1
        intervals = [[seed_start, seed_end]]
        # print(len(intervals))
        next_intervals = []
        for map in maps:
            if len(map) == 0:
                continue
            # print(map)
            for m in map:
                #while len(intervals) > 0:
                # print(len(intervals))
                intervals2 = []
                for interval in intervals:
                    #interval = intervals.pop(0)
                    destination = m[0]
                    l = m[1]
                    r = m[1]+m[2]
                    # print(f"MAP: {l}-{r} {m[0]},{m[2]} || INTERVAL: {interval[0]}-{interval[1]}")
                    if interval[0] < l and interval[1] > l:
                        if interval[1] <= r:
                            # print("IF 1")
                            overlap = interval[1] - l #r - interval[0]
                            next_intervals.append([destination, destination+overlap])
                            intervals2.append([interval[0] ,l-1])
                        else:
                            # print("IF 2")
                            next_intervals.append([destination, destination+m[2]-1])
                            intervals2.append([r+1, interval[1]])
                            intervals2.append([interval[0], l-1])
                    elif interval[0] >= l and interval[0] <= r:
                        if interval[1] > r:
                            # print("IF 3")
                            overlap = r - interval[0]
                            next_intervals.append([destination+m[2]-overlap, destination+m[2]-1]) # TODO -1 maybe
                            intervals2.append([r+1, interval[1]])
                        else:
                            # print("IF 4")
                            l_diff = interval[0] - l
                            r_diff = r - interval[1]
                            interval_range = interval[1] - interval[0]
                            next_intervals.append([destination+l_diff, destination+l_diff+interval_range])
                            # print("NEXT INTERVALS AFTER IF 4:")
                            # print(next_intervals)
                    else:
                        intervals2.append(interval)
                intervals = intervals2

            intervals += next_intervals
            next_intervals = []

        locations += intervals

    print(min(locations))

#part1()
part2()