colors = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt") as f:
    res = 0
    for line in f.read().splitlines():
        game, cubes = line.split(': ')
        g = game.split(' ')[1]

        cubes = cubes.split('; ')
        good = True
        for cube in cubes:
            cube = cube.split(', ')
            for color in cube:
                num, c = color.split(' ')
                if int(num) > colors[c]:
                    good = False
        if good:
            res += int(g)

    print(res)
