def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]

        # Split up in dots and fold instructions
        # Parse the split instructions
        dots = []
        folds = []
        seen_newline = False
        for line in input_list:
            if not line:
                seen_newline = True
            elif not seen_newline:
                temp = line.split(',')
                dots.append([int(temp[0]), int(temp[1])])
            else:
                temp = line.split(' ')[-1].split('=')
                folds.append([temp[0], int(temp[1])])
        return dots, folds


def solution_one():
    dots, folds = parse_input('input.txt')

    for fold in [folds[0]]:
        new_dots = []
        inter = 0 if fold[0] == 'x' else 1
        for dot in dots:
            if dot[inter] < fold[1]:
                new_dots.append(dot)
            else:
                dot[inter] = fold[1] - (dot[inter] - fold[1])
                new_dots.append(dot)

        dots = new_dots

    dots = set(tuple(i) for i in dots)
    return len(dots)


def solution_two():
    dots, folds = parse_input('input.txt')

    for fold in folds:
        new_dots = []
        inter = 0 if fold[0] == 'x' else 1
        for dot in dots:
            if dot[inter] < fold[1]:
                new_dots.append(dot)
            else:
                dot[inter] = fold[1] - (dot[inter] - fold[1])
                new_dots.append(dot)

        dots = new_dots

    max_c = max(dots, key=lambda t: t[1])[1]
    max_r = max(dots, key=lambda t: t[0])[0]

    for c in range(max_c + 1):
        for r in range(max_r + 1):
            if [r, c] in dots:
                print("#", end='')
            else:
                print(" ", end='')
        print("")
    return "Read the output above"


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
