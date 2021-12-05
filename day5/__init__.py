def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]

        # Get the coordinates and convert the coordinates into integers
        coordinates = []
        for item in input_list:
            temp = item.split(' -> ')
            temp2 = [int(e) for e in (temp[0].split(',') + temp[1].split(','))]
            coordinates.append(temp2)

        return coordinates


def coordinates_on_line(x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        return []

    coordinates = []
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            coordinates.append((x1, i))
        return coordinates
    else:
        for i in range(min(x1, x2), max(x1, x2)+1):
            coordinates.append((i, y1))
        return coordinates


def coordinates_on_all_lines(x1, y1, x2, y2):
    if x1 != x2 and y1 != y2 and abs(x1-x2) != abs(y1-y2):
        return []

    coordinates = []
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            coordinates.append((x1, i))
        return coordinates
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            coordinates.append((i, y1))
        return coordinates
    else:
        y = [i for i in range(min(y1, y2), max(y1, y2)+1)]
        if y1 > y2:
            y = y[::-1]
        x = [i for i in range(min(x1, x2), max(x1, x2)+1)]
        if x1 > x2:
            x = x[::-1]

        for i in range(len(y)):
            coordinates.append((x[i], y[i]))
        return coordinates


def solution_one():
    input_list = parse_input('input.txt')
    hydrothermal_vent_count = {}

    for line in input_list:
        cords = coordinates_on_line(line[0], line[1], line[2], line[3])
        for cord in cords:
            if cord in hydrothermal_vent_count:
                hydrothermal_vent_count[cord] += 1
            else:
                hydrothermal_vent_count[cord] = 1

    count = 0
    for key in hydrothermal_vent_count:
        if hydrothermal_vent_count[key] > 1:
            count += 1
    return count


def solution_two():
    input_list = parse_input('input.txt')
    hydrothermal_vent_count = {}

    for line in input_list:
        cords = coordinates_on_all_lines(line[0], line[1], line[2], line[3])
        for cord in cords:
            if cord in hydrothermal_vent_count:
                hydrothermal_vent_count[cord] += 1
            else:
                hydrothermal_vent_count[cord] = 1

    count = 0
    for key in hydrothermal_vent_count:
        if hydrothermal_vent_count[key] > 1:
            count += 1
    return count


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
