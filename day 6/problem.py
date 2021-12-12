from util import read_input

counts = read_input()

def tick(counts : list[int]):
    new_counts = [0 for i in range(9)]

    for i in range(9):
        if i == 0:
            new_counts[6] += counts[i]
            new_counts[8] += counts[i]
        else:
            new_counts[i - 1] += counts[i]
    
    return new_counts


for i in range(80):
    counts = tick(counts)

sum = 0
for count in counts:
    sum += count

print(sum) # answer is 372300

for i in range(256 - 80):
    counts = tick(counts)

sum = 0
for count in counts:
    sum += count

print(sum) # answer is 1675781200288