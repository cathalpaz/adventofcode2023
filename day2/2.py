with open("input.txt") as f:
    res = 0
    for line in f.read().splitlines():
        cubes = line.split(': ')[1]
        cubes = cubes.split('; ')
        maxes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for cube in cubes:
            color = cube.split(', ')
            for side in color:
                num, c = side.split(' ')
                if int(num) > maxes[c]:
                    maxes[c] = int(num)
        power = maxes['red'] * maxes['blue'] * maxes['green']
        res += power

    print(res)
