class Board:
    def __init__(self, numbers : list[list[int]]) -> None:
        self.numbers = numbers
        self.is_marked = [[False for y in range(5)] for x in range(5)]
    
    def mark(self, number : int):
        for x in range(5):
            for y in range(5):
                if self.numbers[x][y] == number:
                    self.is_marked[x][y] = True

    def is_won(self):
        # columns
        for x in range(5):
            if all(self.is_marked[x]):
                return True
        
        # rows
        for y in range(5):
            if all([self.is_marked[x][y] for x in range(5)]):
                return True
        
        if all([self.is_marked[i][i] for i in range(5)]):
            return True
        
        if all([self.is_marked[4 - i][i] for i in range(5)]):
            return True
        
        return False

    def get_unmarked_sum(self):
        sum = 0
        for x in range(5):
            for y in range(5):
                if not self.is_marked[x][y]:
                    sum += self.numbers[x][y]
        
        return sum
    
    def __repr__(self) -> str:
        s = ""
        for x in range(5):
            for y in range(5):
                if(self.numbers[x][y] < 10):
                    s += ' '

                s += str(self.numbers[x][y]) + ' '
            
            s += '    '

            for y in range(5):
                if(self.is_marked[x][y]):
                    s += ' X '
                    continue

                if(self.numbers[x][y] < 10):
                    s += ' '

                s += str(self.numbers[x][y]) + ' '
            
            s += '\n'
        return s

def read_into(numbers : list, boards : list):
    with open('input.txt', 'r') as file:
        line = file.readline()
        
        for s in line.split(','):
            numbers.append(int(s))

        line = file.readline()

        while line:
            board_numbers = [[0, 0, 0, 0, 0] for i in range(5)]
            arr = []

            for y in range(5):
                text = file.readline().split(' ')
                row = []

                for item in text:
                    if item != '':
                        row.append(int(item))
                
                x = 0
                for num in row:
                    board_numbers[x][y] = num
                    x += 1

            boards.append(Board(board_numbers))
            line = file.readline()