from util import Board, read_into

numbers = []
boards: list[Board] = [] 

read_into(numbers, boards)
displayed = []
num_boards = len(boards)
num_wins = 0
done = False

for number in numbers:
    displayed.append(number)
    to_remove = []

    for board in boards:
        board.mark(number)

    for board in boards:
        if board.is_won():
            if num_wins < num_boards - 1:
                to_remove.append(board)
                num_wins += 1
            else:
                print(board.get_unmarked_sum() * number)
                done = True
                break
    
    if done:
        break
    
    for board in to_remove:
        boards.remove(board)
    
    


# answer is 23541