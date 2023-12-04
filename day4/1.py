with open('input.txt') as f:
    res = 0
    for line in f.read().splitlines():
        count = 0
        l = line.split(': ')[1:]
        winning, nums = l[0].split(' | ')
        winning = winning.split(' ')
        winners = set(winning)

        nums = nums.split(' ')
        for n in nums:
            if n and n in winners:
                if not count:
                    count += 1
                else:
                    count *= 2

        res += count

    print(res)
