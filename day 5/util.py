def x1(line):
    return line[0][0]

def x2(line):
    return line[1][0]

def y1(line):
    return line[0][1]

def y2(line):
    return line[1][1]

def read_into(arr : list, filename):
    with open(filename, 'r') as file:
        line = file.readline()

        while line:
            points = line.split(' -> ')
            p1 = points[0].split(',')
            p2 = points[1].split(',')

            x1 = int(p1[0])
            y1 = int(p1[1])
            x2 = int(p2[0])
            y2 = int(p2[1])

            if x1 > x2:
                arr.append( ( (x2, y2), (x1, y1) ) )
            elif x1 == x2 and y1 > y2:
                arr.append( ( (x2, y2), (x1, y1) ) )
            else:
                arr.append( ( (x1, y1), (x2, y2) ) )

            line = file.readline()