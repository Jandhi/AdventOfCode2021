from util import invert, read_into, binary_to_decimal, find_max

arr = []
read_into(arr)

total = 0
bits = len(arr[0])
counts = [0 for i in range(bits)]

for line in arr:
    total += 1
    for index, item in enumerate(line):
        if item == "1":
            counts[index] += 1

def most_common_func(count):
    if count >= total / 2:
        return "1"
    else:
        return "0"

most_common = ""

for count in counts:
    most_common += most_common_func(count)

def common_length(string : str, string2 : str):
    index = 0

    while index < bits and string[index] == string2[index]:
        index += 1
    
    return index

oxy = find_max(arr, lambda x : common_length(x, most_common))
co2 = find_max(arr, lambda x : common_length(x, invert(most_common)))


print(binary_to_decimal(oxy) * binary_to_decimal(co2))