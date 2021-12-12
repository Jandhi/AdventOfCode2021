def read_input() -> list:
    counts = [0 for i in range(9)]
    with open('input.txt', 'r') as file:
        line = file.readline()
        for char in line.split(','):
            counts[int(char)] += 1
    return counts