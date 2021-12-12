def read_into(arr : list):
    with open('input.txt', 'r') as file:
        line = file.readline()
        
        while line:
            arr.append(line[:-1])
            line = file.readline()

def binary_to_decimal(bin : str):
    val = 0
    for index, alpha in enumerate(bin[::-1]):
        if alpha == "1":
            val += 2 ** index
    return val

def find_max(list, function):
    max_item = list[0]
    max_val = function(max_item)

    for item in list[1:]:
        val = function(item)
        if val > max_val:
            max_val = val
            max_item = item
    
    return max_item

def invert(string):
    inverted = ""
    for s in string:
        if s == "1":
            inverted += "0"
        else:
            inverted += "1"
    
    return inverted