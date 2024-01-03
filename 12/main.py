from functools import reduce

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            s = line.split(" ")
            numbers = s[1].split(",")
            input.append(([x for x in s[0]], [int(x) for x in numbers]))
    return input

def check(s, n):
    cn = 0
    for i in range(len(s)):
        if s[i] == ".":
            if cn > 0:
                return False
        elif s[i] == "#":
            if cn == 0 and len(n) == 0:
                return False
            if i == 0:
                cn = n[0] - 1
                n = n[1:]
            elif s[i-1] == "#" and cn == 0:
                return False
            elif s[i-1] == "#":
                cn -= 1
            else:
                cn = n[0] - 1
                n = n[1:]
    if cn == 0 and len(n) == 0:
        return True
    else:
        return False

def rec(sequence, i, number, numbers):
    if len(numbers) == 0 and number == 0:
        # print(" == 0")
        if all(x != "#" for x in sequence[i:]):
            # print("OPTION!")
            # print(sequence)
            global full_numbers
            chck = check(sequence, full_numbers)
            if not chck:
                print("ERROR!!!")
                print(sequence)
                print(full_numbers)
            return 1
    if i >= len(sequence):
        # print("i > len")
        return 0
    if sequence[i] == "." and number == 0:
        # print(". and 0")
        return rec(sequence, i+1, number, numbers)
    if sequence[i] == "#":
        if number > 0:
            # print("# num > 0")
            return rec(sequence, i+1, number-1, numbers)
        elif sequence[i-1] != "#" and len(numbers) > 0:
            # print("# i-1 != #")
            # next_number = numbers[0]-1 if len(numbers) > 0 else 0
            return rec(sequence, i+1, numbers[0]-1, numbers[1:])
    if sequence[i] == "?":
        if number == 0:
            if i == 0 or (i != 0 and sequence[i-1] != "#"):
                # print("? num == 0 BIG")
                count = 0
                # Can put # here
                if len(numbers) > 0:
                    sequence[i] = "#"
                    # next_number = numbers[0]-1 if len(numbers) > 0 else 0
                    count += rec(sequence, i+1, numbers[0]-1, numbers[1:])
                    sequence[i] = "?"
                # Can not put # here
                sequence[i] = "."
                count += rec(sequence, i+1, 0, numbers)
                sequence[i] = "?"
                return count
            else:
                # print("? num == 0 ELSE")
                # Have to put "." here
                sequence[i] = "."
                count = rec(sequence, i+1, 0, numbers)
                sequence[i] = "?"
                return count
        elif sequence[i-1] == "#":
            # print("? i-1 == #")
            # print(f"{sequence} {i} {number} {numbers}")
            # Have to add another #
            sequence[i] = "#"
            count = rec(sequence, i+1, number-1, numbers)
            sequence[i] = "?"
            return count
        else:
            # print("??? ELSE")
            # ????
            return 0
    return 0   
    
full_numbers = []

def part1():
    # 6860 too high
    # 6431 too low
    # 6432 too low
    inputs = read_input("1.txt")
    global full_numbers
    possible_sequences = []
    for (input, numbers) in inputs:
        # print(f"INPUT: {input}")
        full_numbers = numbers
        possible_sequences.append(rec(input, 0, 0, numbers))
    print(sum(possible_sequences))
    


def part2():
    gmap = read_input("test.txt")
    

    
part1()
part2()

