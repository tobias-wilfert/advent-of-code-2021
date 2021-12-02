def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1].split(' ') for i in input_list]
        return input_list


def solution_one():
    input_list = parse_input('input.txt')
    x, y = 0, 0

    for move in input_list:
        if move[0] == 'forward':
            y += int(move[1])
        elif move[0] == 'down':
            x += int(move[1])
        elif move[0] == 'up':
            x -= int(move[1])

    return x * y


def solution_two():
    input_list = parse_input('input.txt')
    x, y, aim = 0, 0, 0

    for move in input_list:
        if move[0] == 'forward':
            y += int(move[1])
            x += int(move[1])*aim
        elif move[0] == 'down':
            aim += int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])

    return x * y


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
