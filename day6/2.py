with open('input.txt') as f:
    time, distance = f.read().splitlines()

    time = ''.join(time.split(':   ')[1].split('     ')[1:])
    distance = ''.join(distance.split(':   ')[1].split('   '))

    res = 0

    # two pointers:
    i, j = 1, int(time) - 1
    first, last = None, None
    while (i < j) and (not first and not last):
        if i * (int(time) - i) >= int(distance):
            first = i
        else:
            i += 1

        if j * (int(time) - j) >= int(distance):
            last = j
        else:
            j -= 1

    print(last - first + 1)
