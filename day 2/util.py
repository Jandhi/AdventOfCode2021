
def read_into(arr : list[tuple[str, int]]):
    with open('input.txt', 'r') as file:
        line = file.readline()
        while line:
            parts = line.split(' ')
            text = parts[0]
            number = parts[1]

            arr.append((text, int(number)))
            line = file.readline()