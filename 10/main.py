from functools import reduce
import math

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            x = []
            for c in line:
                x.append(c)
            input.append(x)

    
    return input

def find_start(field):
    for ii, i in enumerate(field):
        for jj, j in enumerate(i):
            if j == "S":
                return (ii, jj)

def part1():
    field = read_input("1.txt")
    (i, j) = find_start(field)

    steps = 1
    dir = "X"
    if i > 0 and field[i-1][j] in ["|", "7", "F"]:
        i -= 1
        dir = "U"
    elif j > 0 and field[i][j-1] in ["-", "L", "F"]:
        j -= 1
        dir = "L"
    elif i < len(field)-1 and field[i+1][j] in ["|", "L", "J"]:
        i += 1
        dir = "D"
    elif j < len(field[0])-1 and field[i][j+1] in ["-", "J", "7"]:
        j += 1
        dir = "R"

    while field[i][j] != "S":
        match field[i][j]:
            case "|":
                if dir == "U":
                    i -= 1
                else: 
                    i += 1
            case "-":
                if dir == "L":
                    j -= 1
                else: 
                    j += 1
            case "L":
                if dir == "D":
                    j += 1
                    dir = "R"
                else: 
                    i -= 1
                    dir = "U"
            case "J":
                if dir == "D":
                    j -= 1
                    dir = "L"
                else: 
                    i -= 1
                    dir = "U"
            case "7":
                if dir == "R":
                    i += 1
                    dir = "D"
                else: 
                    j -= 1
                    dir = "L"
            case "F":
                if dir == "U":
                    j += 1
                    dir = "R"
                else: 
                    i += 1
                    dir = "D"
        steps += 1

    print(f"{steps/2} ceiled as {math.ceil(steps/2)}")  
   

def part2():
    field = read_input("test.txt")
    

    
part1()
part2()