from util import read_into

arr = []
read_into(arr)

horizontal_position = 0
aim = 0
depth = 0

for entry in arr:
    text, number = entry

    if text == "forward":
        horizontal_position += number
        depth += aim * number
    elif text == "down":
        aim += number
    elif text == "up":
        aim -= number

print(horizontal_position * depth)
# answer is 2044620088