
def read_into(list : list):
    with open('input.txt', 'r') as file:
        line = file.readline()
        while line:
            list.append(int(line))
            line = file.readline()