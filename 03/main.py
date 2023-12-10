from functools import reduce

def read_input(filename):
    input = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            input.append(line.replace("\n", ""))      
    return input

def is_adjacent_to_symbol(schematic, x, y) -> bool:
    if x > 0 and not schematic[x-1][y].isnumeric() and schematic[x-1][y] != '.':
        return True
    if x+1 < len(schematic) and not schematic[x+1][y].isnumeric() and schematic[x+1][y] != '.':
        return True
    if y > 0 and not schematic[x][y-1].isnumeric() and schematic[x][y-1] != '.':
        return True
    if y+1 < len(schematic[x]) and not schematic[x][y+1].isnumeric() and schematic[x][y+1] != '.':
        return True
    
    if x > 0 and y > 0 and not schematic[x-1][y-1].isnumeric() and schematic[x-1][y-1] != '.':
        return True
    if x+1 < len(schematic) and y+1 < len(schematic[0]) and not schematic[x+1][y+1].isnumeric() and schematic[x+1][y+1] != '.':
        return True
    if x > 0 and y+1 < len(schematic[0]) and not schematic[x-1][y+1].isnumeric() and schematic[x-1][y+1] != '.':
        return True
    if x+1 < len(schematic) and y > 0 and not schematic[x+1][y-1].isnumeric() and schematic[x+1][y-1] != '.':
        return True
    
    return False

def part1():
    schematic = read_input("1.txt")

    numbers = []

    for x, line in enumerate(schematic):
        start = -1
        end = -1
        i = 0
        while i < len(line):
            if line[i].isnumeric():
                valid_number = False
                if start == -1:
                    start = i  
                    while i < len(line) and line[i].isnumeric():
                        if not valid_number: 
                            valid_number = is_adjacent_to_symbol(schematic, x, i)
                        end = i
                        i += 1
                if valid_number:
                    numbers.append(int(line[start:end+1]))
                start = -1
                end = -1
            i += 1
    
    print(sum(numbers))

def generate_coordinates_around(schematic, x, y, distance=1):
    coordinates = []
    for i in range(x - distance, x + distance + 1):
        for j in range(y - distance, y + distance + 1):
            if x == i and y == j:
                continue
            if i >= 0 and j >= 0 and i < len(schematic) and j < len(schematic[0]):
                coordinates.append((i, j))
    return coordinates
 
def part2():
    schematic = read_input("1.txt")

    numbers = []

    for x, line in enumerate(schematic):
        # Find gear (*)
        for y, v in enumerate(line):
            if v == "*":
                # Gear! Find numbers
                gear_numbers = []
                coordinates = generate_coordinates_around(schematic, x, y)
                checked_coordinates = []
                for c in coordinates:
                    i = c[0]
                    j = c[1]
                    if (i,j) in checked_coordinates:
                        continue
                    if schematic[i][j].isnumeric():
                        # Find this number
                        left = j
                        right = j
                        checked_coordinates.append((i, left))
                        while left >= 0 and schematic[i][left].isnumeric():
                            left -= 1
                            checked_coordinates.append((i, left))
                        left += 1
                        while right < len(schematic[0]) and schematic[i][right].isnumeric():
                            right += 1
                            checked_coordinates.append((i, right))
                        gear_numbers.append(int(schematic[i][left:right]))
                
                print(gear_numbers)
                if len(gear_numbers) == 2:
                    numbers.append(gear_numbers[0] * gear_numbers[1])

    
    print(sum(numbers))

part2()