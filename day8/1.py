inp = []
with open("input.txt") as f:
    for line in f.read().splitlines():
        inp.append(line)

directions = inp[0]
ele = inp[2:]

# key -> network, value -> tuple
networks = {}
for e in ele:
    k, v = e.split(' = ')
    l, r = v[1:-1].split(', ')
    networks[k] = (l, r)


current = 'AAA'
step_idx = 0
steps = 0
while current != 'ZZZ':
    if directions[step_idx] == 'L':
        current = networks[current][0]
    else:
        current = networks[current][1]

    steps += 1
    step_idx += 1

    if step_idx == len(directions):
        step_idx = 0

print(steps)
