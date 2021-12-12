from util import read_into

arr = []
read_into(arr)

horizontal_position = 0
depth = 0

for entry in arr:
    text, number = entry

    if text == "forward":
        horizontal_position += number
    elif text == "down":
        depth += number
    elif text == "up":
        depth -= number

print(horizontal_position * depth)
# answer is 2147104