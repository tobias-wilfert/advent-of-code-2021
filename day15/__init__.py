import queue


def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [list(i[:-1]) for i in input_list]

        for row in range(len(input_list)):
            for col in range(len(input_list[0])):
                input_list[row][col] = int(input_list[row][col])

        return input_list


def neighbours(r, c, h, l):
    n = []
    if r-1 >= 0:
        n.append([r-1, c])
    if c-1 >= 0:
        n.append([r, c-1])
    if r+1 < h:
        n.append([r+1, c])
    if c+1 < l:
        n.append([r, c+1])
    return n


def solution_one():
    # Get the input
    field = parse_input('input.txt')
    # Keep track of the visited fields
    visited = set()
    # Construct and populate the priority queue
    q = queue.PriorityQueue()
    for neighbour in neighbours(0, 0, len(field), len(field[0])):
        q.put((field[neighbour[0]][neighbour[1]], neighbour))

    # While there are still states to explore
    while not q.empty():
        cur = q.get()
        # Skip over any visited states
        p = tuple(cur[1])
        while p in visited:
            cur = q.get()
            p = tuple(cur[1])
        visited.add(p)
        # Check if cur is the final state
        if cur[1][0] == len(field)-1 and cur[1][1] == len(field[0])-1:
            return cur[0]
        # Else add the neighbours
        for neighbour in neighbours(cur[1][0], cur[1][1], len(field), len(field[0])):
            q.put((field[neighbour[0]][neighbour[1]]+cur[0], neighbour))
    return -1


def solution_two():
    # Get the input
    field = parse_input('input.txt')
    # Need to increase the field size
    w = len(field[0])
    h = len(field)
    # First make it the correct length, then make it the correct hight
    for row in range(len(field)):
        for i in range(1, 5):
            for j in range(w):
                t = (field[row][j] + i)
                field[row].append(t if t <= 9 else t-9)

    for i in range(1, 5):
        for r in range(h):
            field.append(list())
            for j in range(len(field[0])):
                t = (field[r][j] + i)
                field[-1].append(t if t <= 9 else t-9)

    # Keep track of the visited fields
    visited = set()
    # Construct and populate the priority queue
    q = queue.PriorityQueue()
    for neighbour in neighbours(0, 0, len(field), len(field[0])):
        q.put((field[neighbour[0]][neighbour[1]], neighbour))

    # While there are still states to explore
    while not q.empty():
        cur = q.get()
        # Skip over any visited states
        p = tuple(cur[1])
        while p in visited:
            cur = q.get()
            p = tuple(cur[1])
        visited.add(p)
        # Check if cur is the final state
        if cur[1][0] == len(field) - 1 and cur[1][1] == len(field[0]) - 1:
            return cur[0]
        # Else add the neighbours
        for neighbour in neighbours(cur[1][0], cur[1][1], len(field), len(field[0])):
            q.put((field[neighbour[0]][neighbour[1]] + cur[0], neighbour))
    return -1


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
