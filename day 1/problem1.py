from util import read_into

arr = []
read_into(arr)

prev = None
increases = 0
for num in arr:
    if prev and prev < num:
        increases += 1

    prev = num

print(increases)
# answer is 1477