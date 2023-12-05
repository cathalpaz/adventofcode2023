# def symbol(i, j):
#     if not (0 <= i < n and 0 <= j < m):
#         return False

#     return lines[i][j] != '.' and not lines[i][j].isdigit()

with open('input.txt') as f:
    lines = f.read().splitlines()
    def symbol(i, j):
        if not (0 <= i < len(lines) and 0 <= j < len(lines[0])):
            return False

        return lines[i][j] != '.' and not lines[i][j].isdigit()

    res = 0

    for i, line in enumerate(lines):
        start = 0
        j = 0

        while j < len(lines):
            start = j
            num = ''
            while j < len(line) and line[j].isdigit():
                num += line[j]
                j += 1

            if num == '':
                j += 1
                continue

            num = int(num)

            if symbol(i, start - 1) or symbol(i, j):
                res += num
                continue

            for k in range(start - 1, j + 1):
                if symbol(i - 1, k) or symbol(i + 1, k):
                    res += num
                    break
    print(res)
