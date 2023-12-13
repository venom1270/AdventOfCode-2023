from functools import reduce

def read_input(filename):
    times = []
    distances = []
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        numbers_line = " ".join(lines[0].split(":")[1].strip().split())
        distances_line = " ".join(lines[1].split(":")[1].strip().split())
        times = [int(x) for x in numbers_line.split(" ")]
        distances = [int(x) for x in distances_line.split(" ")]

    return (times, distances)

def read_input_part2(filename):
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        numbers_line = " ".join(lines[0].split(":")[1].strip().split())
        distances_line = " ".join(lines[1].split(":")[1].strip().split())
        return (int(numbers_line.replace(" ", "")), int(distances_line.replace(" ", "")))


def part1():
    (times, distances) = read_input("1.txt")
    ways_to_win = []
    for (time, distance) in zip(times,distances):
        wins = 0
        for i in range(1, time):
            time_left = time - i
            if distance < time_left * i:
                wins += 1
        ways_to_win.append(wins)

    margin = reduce(lambda x, y: x*y, ways_to_win)
    print(margin)
   

def part2():
    (time, distance) = read_input_part2("1.txt") 
    wins = 0
    for i in range(1, time):
        time_left = time - i
        if distance < time_left * i:
            wins += 1
    print(wins)

part1()
part2()