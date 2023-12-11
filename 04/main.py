def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            s = line.split(" | ")
            winning_string = s[0].split(": ")[1]
            winning_split = " ".join(winning_string.split()).split(" ")
            numbers_split = " ".join(s[1].split()).split(" ")
            input.append(([int(x) for x in winning_split], [int(x) for x in numbers_split]))
    return input


def part1():
    scratchcards = read_input("1.txt")
    values = []
    for s in scratchcards:
        val = 0
        for number in s[1]:
            if number in s[0]:
                if val == 0:
                    val = 1
                else:
                    val *= 2
        values.append(val)    
    print(sum(values))

def part2():
    scratchcards = read_input("1.txt")
    scratchcards = [(i, x, y) for i, (x,y) in enumerate(scratchcards)]
    num_scratchcards = len(scratchcards)
    copy_map = {}
    for (i, winning, numbers) in scratchcards:
        val = 0
        for number in numbers:
            if number in winning:
                val += 1
        num_scratchcards += val
        if i in copy_map:
            scratchcards += copy_map[i]
        else:
            copy_map[i] = []
            for j in range(val):
                scratchcards.append(scratchcards[i+j+1])
                copy_map[i].append(scratchcards[i+j+1])
    #print(copy_map)
    print(num_scratchcards)

part1()
part2()