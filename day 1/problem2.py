from util import read_into

arr = []
read_into(arr)

prev3 = None
prev2 = None
prev1 = None
increases = 0

for num in arr:
    if prev1 and prev2 and prev3:
        if prev1 + prev2 + prev3 < num + prev1 + prev2:
            increases += 1

    prev3 = prev2
    prev2 = prev1
    prev1 = num

print(increases)
# answer is 1523