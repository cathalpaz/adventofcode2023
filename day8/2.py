from math import gcd

lines = []
with open("input.txt") as f:
    for line in f.read().splitlines():
        lines.append(line)

directions = lines[0]

networks = {}
current_nodes = []
for e in lines[2:]:
    k, v = e.split(' = ')
    if k.endswith('Z') == 'A':
        current_nodes.append(k)
    l, r = v[1:-1].split(', ')
    networks[k] = (l, r)

cycles = []

for current in current_nodes:
    cycle = []
    current_steps = directions
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = networks[current][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)
