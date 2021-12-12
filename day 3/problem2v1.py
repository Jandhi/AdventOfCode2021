from util import read_into, binary_to_decimal

arr = []
read_into(arr)

print(len(arr))

num_bits = len(arr[0])
total = 0
counts = [0 for i in range(num_bits)]

for line in arr:
    total += 1
    for index, item in enumerate(line):
        if item == "1":
            counts[index] += 1

arr2 = arr.copy()

one_is_more_common = [count >= total / 2 for count in counts]
index = 0
while len(arr) > 1:
    if one_is_more_common[index]:
        # filter 0s
        arr = list(filter(lambda x : x[index] == "1", arr))
    else:
        # filter 1s
        arr = list(filter(lambda x : x[index] == "0", arr))
    index += 1
oxygen_generator_rating = binary_to_decimal(arr[0])

zero_is_less_common = [count <= total / 2 for count in counts]
index = 0
while len(arr2) > 1:
    if zero_is_less_common[index]:
        arr2 = list(filter(lambda x : x[index] == "1", arr2))
    else:
        arr2 = list(filter(lambda x : x[index] == "0", arr2))
    index += 1
CO2_scrubber_rating = binary_to_decimal(arr2[0])

print(oxygen_generator_rating * CO2_scrubber_rating)