with open("input.txt") as f:
    res = 1

    time, distance = f.read().splitlines()

    print(time, distance)
    times = time.split(':   ')[1].split('     ')[1:]
    distances = distance.split(':   ')[1].split('   ')

    for i in range(len(times)):
        count = 0
        for j in range(1, int(times[i])):
            if j * (int(times[i]) - j) >= int(distances[i]):
                count += 1

        res *= count

    print(res)
