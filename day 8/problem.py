
zero  = 'abcefg'
one   = 'cf'
two   = 'acdeg'
three = 'acdfg'
four  = 'bcdf'
five  = 'abdfg'
six   = 'abdefg'
seven = 'acf'
eight = 'abcdefg'
nine  = 'abcdfg'

signal_to_digit = {
    zero : '0',
    one : '1',
    two : '2',
    three : '3',
    four : '4',
    five : '5',
    six : '6',
    seven : '7',
    eight : '8',
    nine : '9'
}

a_count = 8
b_count = 6
c_count = 8
d_count = 7
e_count = 4
f_count = 9
g_count = 7

lines = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        parts = line.split('|')
        
        signals = parts[0].split(' ')[:-1]        
        output = parts[1][:-1].split(' ')[1:]

        lines.append((signals, output))

        line = file.readline()

ones = 0
fours = 0
sevens = 0
eights = 0

for line in lines:
    signals, output = line
    for number in output:
        if len(number) == 2:
            ones += 1
        elif len(number) == 3:
            sevens += 1
        elif len(number) == 4:
            fours += 1
        elif len(number) == 7:
            eights += 1

print(ones + fours + sevens + eights) # answer is 301

sum = 0

def find_letter_by_count(letter_counts : dict, value):
    for letter, count in letter_counts.items():
        if count == value:
            return letter

def find_letters_by_count(letter_counts : dict, value):
    letters = []
    for letter, count in letter_counts.items():
        if count == value:
            letters.append(letter)
    
    return letters

for line in lines:
    signals, output = line

    codes_by_length : dict[int, list] = {}
    letter_counts = {x : 0 for x in 'abcdefg'}
    
    for signal in signals:
        length = len(signal)

        if not length in codes_by_length:
            codes_by_length[length] = []
        
        codes_by_length[length].append(sorted(signal))

        for letter in signal:
            letter_counts[letter] += 1
    
    coded_one = codes_by_length[2][0]
    coded_seven = codes_by_length[3][0]

    a = list(filter(lambda x : x not in coded_one, coded_seven))[0]
    b = find_letter_by_count(letter_counts, 6)
    e = find_letter_by_count(letter_counts, 4)
    f = find_letter_by_count(letter_counts, 9)

    c = list(filter(lambda x : x != a, find_letters_by_count(letter_counts, 8)))[0]
    
    dg = find_letters_by_count(letter_counts, 7)
    d = '?'
    g = '?'
    counts = [0, 0]

    for signal in codes_by_length[6]:
        if dg[0] in signal:
            counts[0] += 1
        if dg[1] in signal:
            counts[1] += 1

    if counts[0] > counts[1]:
        d = dg[1]
        g = dg[0]
    else:
        d = dg[0]
        g = dg[1]

    decode = {
        a : 'a',
        b : 'b',
        c : 'c',
        d : 'd',
        e : 'e',
        f : 'f',
        g : 'g'
    }

    output_string = ''

    for out in output:
        decoded = ''
        for letter in out:
            decoded += decode[letter]
        sorted_decoded = ''
        for letter in sorted(decoded):
            sorted_decoded += letter
        output_string += signal_to_digit[sorted_decoded]
    
    sum += int(output_string)

print(sum) # answer is 908067


