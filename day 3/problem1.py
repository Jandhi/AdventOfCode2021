from util import read_into

arr = []
read_into(arr)

num_bits = len(arr[0])
total = 0
counts = [0 for i in range(num_bits)]

for line in arr:
    total += 1
    for index, item in enumerate(line[::-1]):
        if item == "1":
            counts[index] += 1

gamma_rate = 0
epsilon_rate = 0

for index, item in enumerate(counts):
    if item > total / 2:
        gamma_rate += 2 ** index
    else:
        epsilon_rate += 2 ** index

print(gamma_rate * epsilon_rate)
# answer is 693486