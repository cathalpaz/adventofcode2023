with open("input.txt") as f:
    res = 0
    for line in f.read().splitlines():
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        res += int(digits[0] + digits[-1])
    print(res)
