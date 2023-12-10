from functools import reduce

def read_input(filename):
    games = []
    with open(filename, "r", encoding="utf8") as f:
        for line in f.readlines():
            s = line.split(":")
            id = int(s[0].split(" ")[1])
            split_games = s[1].split(";")
            colors_in_game = []
            for sp in split_games:
                split_colors = sp.split(",")
                colors = [0, 0, 0]
                for c in split_colors:
                    num_color = c[1:].split(" ")
                    num_color[1] = num_color[1].replace(" ", "").replace("\n", "")
                    if num_color[1] == "red":
                        colors[0] = int(num_color[0])
                    elif num_color[1] == "green":
                        colors[1] = int(num_color[0])
                    else:
                        colors[2] = int(num_color[0])
                colors_in_game.append(colors)
            games.append((id, colors_in_game))
    return games



def part1():
    games = read_input("1.txt")
    
    MAX_COLORS = [12, 13, 14]

    sum = 0
    for g in games:
        valid_game = True
        for colors in g[1]:
            for i in range(len(colors)):
                if colors[i] > MAX_COLORS[i]:
                    valid_game = False
            if not valid_game:
                break
        if valid_game:
            print(g[0])
            sum += g[0]

    print(f"Sum: {sum}")

def part2():
    games = read_input("1.txt")
    
    sum = 0
    for g in games:
        MIN_CUBES = [0, 0, 0]
        for colors in g[1]:
            for i in range(len(colors)):
                if colors[i] > MIN_CUBES[i]:
                    MIN_CUBES[i] = colors[i]
        sum += reduce(lambda x, y: x * y, MIN_CUBES)

    print(f"Sum power: {sum}")

    
part2()