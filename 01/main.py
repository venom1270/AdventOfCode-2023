def read_input(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.readlines()



def part1():
    input = read_input("1.txt")
    sum = 0
    for i in input:
        left = 0
        while not i[left].isnumeric():
            left += 1
        right = len(i) - 1
        while not i[right].isnumeric():
            right -=1
        sum += int(i[left]) * 10 + int(i[right])

    print(sum)

def part2():
    input = read_input("1.txt")
    valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0
    for i in input:
        left_digit = -1
        right_digit = -1
        left = 0
        while not i[left].isnumeric() and left_digit == -1:
            for v in valid_digits:
                digit_candidate = i[left:left+len(v)]
                if digit_candidate in valid_digits:
                    left_digit = valid_digits.index(digit_candidate) + 1
            left += 1
        right = len(i) - 1
        while not i[right].isnumeric() and right_digit == -1:
            for v in valid_digits:
                if right + len(v) > len(i):
                    continue
                digit_candidate = i[right:right+len(v)]
                if digit_candidate in valid_digits:
                    right_digit = valid_digits.index(digit_candidate) + 1
            right -=1
        if left_digit == -1:
            left_digit = int(i[left])
        if right_digit == -1:
            right_digit = int(i[right])
        sum += left_digit * 10 + right_digit

    print(sum)

part2()