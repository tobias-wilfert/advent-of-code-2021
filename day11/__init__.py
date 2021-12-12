import queue


def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [list(i[:-1]) for i in input_list]
        input_list = [[int(i) for i in l] for l in input_list]
        return input_list


def neighbours(r, c, h, l):
    n = []
    if r-1 >= 0:
        n.append((r-1, c))
    if c-1 >= 0:
        n.append((r, c-1))
    if r+1 < h:
        n.append((r+1, c))
    if c+1 < l:
        n.append((r, c+1))

    if r-1 >= 0 and c-1 >= 0:
        n.append((r-1, c-1))
    if c-1 >= 0 and r+1 < h:
        n.append((r+1, c-1))
    if r+1 < h and c+1 < l:
        n.append((r+1, c+1))
    if c+1 < l and r-1 >= 0:
        n.append((r-1, c+1))
    return n


def solution_one():
    input_list = parse_input('input.txt')
    trigger = queue.Queue()
    counter = 0

    for i in range(100):
        # Loop over all the numbers and add 1
        # If the number is bigger than 9 add it to a queue
        for r in range(len(input_list)):
            for c in range(len(input_list[0])):
                input_list[r][c] += 1
                if input_list[r][c] > 9:
                    trigger.put((r, c))
                    counter += 1
                    input_list[r][c] = -10  # So that it can't tigger again

        while not trigger.empty():
            cur_r, cur_c = trigger.get()
            # Increase the counter and add 1 to the neighbours check if they trigger if yes add them and add 1
            for neigh in neighbours(cur_r, cur_c, len(input_list), len(input_list[0])):
                n_r, n_c = neigh
                input_list[n_r][n_c] += 1
                if input_list[n_r][n_c] > 9:
                    trigger.put((n_r, n_c))
                    counter += 1
                    input_list[n_r][n_c] = -10  # So that it can't tigger again

        for r in range(len(input_list)):
            for c in range(len(input_list[0])):
                if input_list[r][c] < 0:
                    input_list[r][c] = 0
    return counter


def solution_two():
    input_list = parse_input('input.txt')
    trigger = queue.Queue()
    counter = 0
    t = 1

    while True:
        old_counter = counter
        # Loop over all the numbers and add 1
        # If the number is bigger than 9 add it to a queue
        for r in range(len(input_list)):
            for c in range(len(input_list[0])):
                input_list[r][c] += 1
                if input_list[r][c] > 9:
                    trigger.put((r, c))
                    counter += 1
                    input_list[r][c] = -10  # So that it can't tigger again

        while not trigger.empty():
            cur_r, cur_c = trigger.get()
            # Increase the counter and add 1 to the neighbours check if they trigger if yes add them and add 1
            for neigh in neighbours(cur_r, cur_c, len(input_list), len(input_list[0])):
                n_r, n_c = neigh
                input_list[n_r][n_c] += 1
                if input_list[n_r][n_c] > 9:
                    trigger.put((n_r, n_c))
                    counter += 1
                    input_list[n_r][n_c] = -10  # So that it can't tigger again

        for r in range(len(input_list)):
            for c in range(len(input_list[0])):
                if input_list[r][c] < 0:
                    input_list[r][c] = 0
        if counter - old_counter == len(input_list) * len(input_list[0]):
            return t
        t += 1


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
