def read():
    with open('input.txt') as file:
        line = file.readline()
        return [int(num) for num in line.split(',')]

list = read()

min_val = min(list)
max_val = max(list)

min_pos = None
min_cost = None

for i in range(min_val, max_val):
    fuel_cost = 0

    for num in list:
        fuel_cost += abs(i - num)
    
    if min_pos == None or min_cost > fuel_cost:
        min_cost = fuel_cost
        min_pos = i

print(min_cost) # answer is 349812

min_pos = None
min_cost = None

def series_sum(num):
    return num * (num + 1) / 2

for i in range(min_val, max_val):
    fuel_cost = 0

    for num in list:
        fuel_cost += series_sum(abs(i - num))
    
    if min_pos == None or min_cost > fuel_cost:
        min_cost = fuel_cost
        min_pos = i

print(min_cost) # answer is 99763899