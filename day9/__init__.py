import queue


def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]
        return input_list


def is_lower(r, c, field):
    if r-1 >= 0 and field[r][c] >= field[r-1][c]:
        return False
    if c-1 >= 0 and field[r][c] >= field[r][c-1]:
        return False
    if r+1 < len(field) and field[r][c] >= field[r+1][c]:
        return False
    if c+1 < len(field[0]) and field[r][c] >= field[r][c+1]:
        return False
    return True


def solution_one():
    input_list = parse_input('test.txt')
    risk_level = 0
    for r in range(len(input_list)):
        for c in range(len(input_list[0])):
            # Check if lower than the surrounding
            # Increment the counter if it is the case
            if is_lower(r, c, input_list):
                risk_level += (1 + int(input_list[r][c]))

    return risk_level


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
    return n


def basin_size(r,c, field):
    q = queue.Queue()
    h = len(field)
    l = len(field[0])
    size = 0
    q.put((r, c))
    while not q.empty():
        cur_r, cur_c = q.get()
        if field[cur_r][cur_c] not in ['9', 'x']:
            li = list(field[cur_r])
            li[cur_c] = 'x'
            field[cur_r] = "".join(li)
            size += 1
            for n in neighbours(cur_r, cur_c, h, l):
                q.put(n)
    return size


def solution_two():
    input_list = parse_input('input.txt')
    basins = []
    # BFS the basin until we find a 9
    # Keep track of the size of each basin
    for r in range(len(input_list)):
        for c in range(len(input_list[0])):
            # Check we have not yet examined the position
            if input_list[r][c] not in ['9', 'x']:
                basins.append(basin_size(r, c, input_list))

    basins.sort()
    return basins[-1]*basins[-2]*basins[-3]


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
