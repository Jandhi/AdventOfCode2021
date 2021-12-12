from util import Board, read_into

numbers = []
boards: list[Board] = [] 

read_into(numbers, boards)
win = False
displayed = []

def display(boards, numbers):
    for board in boards:
        print(board)
    
    print(numbers)

for number in numbers:
    displayed.append(number)

    for board in boards:
        board.mark(number)

    for board in boards:
        if board.is_won():
            win = True
            print(board.get_unmarked_sum() * number)
            break
    
    if win:
        break


# answer is 63424