def read_input():
    with open('input.txt', 'r') as f:
        lines = f.read()
        lines = lines.split('\n')[:-1]
        return lines


##### HERE #####
def program(lines):
    res = 0
    for line in lines:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        total = int(digits[0] + digits[-1])
        res += total

    return res



def main():
    lines = read_input()
    solution = program(lines)
    print(solution)

if __name__ == "__main__":
    main()
