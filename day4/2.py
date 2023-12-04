from collections import defaultdict


with open('input.txt') as f:
    multipliers = defaultdict(int)
    for i, line in enumerate(f.read().splitlines()):
        multipliers[i] += 1
        card, numbers = line.split(': ')
        card = card.split(' ')[-1]

        winnings, numbers = numbers.split(' | ')
        winnings, numbers = winnings.split(' '), numbers.split(' ')
        winners = set(winnings)
        count = 0
        for n in numbers:
            if n and n in winners:
                count += 1

        for j in range(count):
            multipliers[i+1+j] += multipliers[i]


    print(sum(multipliers.values()))
