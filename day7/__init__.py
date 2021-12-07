def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = input_list[0][:-1].split(',')
        input_list = [int(i) for i in input_list]
        return input_list


def solution_one():
    input_list = parse_input('input.txt')

    best = -1
    for i in range(max(input_list)):
        cur = 0
        for j in input_list:
            cur += abs(j-i)

        if best == -1 or cur < best:
            best = cur
        elif cur > best:
            break

    return best


def solution_two():
    input_list = parse_input('input.txt')

    best = -1
    for i in range(max(input_list)):
        cur = 0
        for j in input_list:
            n = abs(j - i)
            cur += n * (n + 1) / 2

        if best == -1 or cur < best:
            best = cur
        elif cur > best:
            break

    return best


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
