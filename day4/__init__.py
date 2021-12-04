class Board:
    def __init__(self, board):
        self.board = board  # Copy of the board
        self.map = {}  # Map that keeps track of were in the board we can find a number
        self.score = 0   # Score keeps track of the score of the board
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.map[board[r][c]] = (r, c)
                self.score += int(board[r][c])

    def update(self, number):
        if number in self.map:
            r, c = self.map[number]
            self.board[r][c] = ''
            self.score -= int(number)

    def isComplete(self):
        # Check all rows
        for row in self.board:
            if row.count('') == len(row):
                return True

        # Check all columns
        for c in range(len(self.board)):
            col = [self.board[r][c] for r in range(len(self.board))]
            if col.count('') == len(col):
                return True

        # Check the diagonals
        # d1 = [self.board[x][x] for x in range(len(self.board))]
        # if d1.count('') == len(d1):
        #    return True
        # d2 = [self.board[x][len(self.board) - x - 1] for x in range(len(self.board))]
        # if d2.count('') == len(d2):
        #    return True
        return False


def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]

        # Grab the numbers from this
        bingo_numbers = input_list[0].split(',')

        # Grab the boards from this
        bingo_fields = []
        cur_field = []
        input_list.append('')
        for i in range(2, len(input_list)):
            if input_list[i] == '':
                bingo_fields.append(cur_field)
                cur_field = []
            else:
                cur_field.append(input_list[i].split(' '))

        # Need to remove the empty entries in the bingo_fields
        for i in range(len(bingo_fields)):
            for j in range(len(bingo_fields[i])):
                bingo_fields[i][j] = list(filter(None, bingo_fields[i][j]))

        return bingo_numbers, bingo_fields


def solution_one():
    numbers, fields = parse_input('input.txt')
    boards = [Board(field) for field in fields]

    for num in numbers:
        for board in boards:
            board.update(num)
            if board.isComplete():
                return board.score * int(num)


def solution_two():
    numbers, fields = parse_input('input.txt')
    boards = [Board(field) for field in fields]

    # Keep track of the indices of finished boards
    finished_boards = []
    for num in numbers:
        for i in range(len(boards)):
            if i in finished_boards:  # If the board is finished we can skip it
                continue
            boards[i].update(num)
            if boards[i].isComplete():
                finished_boards.append(i)  # Add the board to the finished boards
                if len(finished_boards) == len(boards):  # If there are as many finished boards as boards in total
                    return boards[i].score * int(num)  # Return the value as we know it is the last board


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
