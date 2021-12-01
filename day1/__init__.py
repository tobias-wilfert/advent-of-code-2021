def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [int(i[:-1]) for i in input_list]
        return input_list


def solution_one():
    input_list = parse_input('input.txt')
    # print(input_list)

    count = 0
    for i in range(1, len(input_list)):
        count += (input_list[i-1] < input_list[i])
    return count


def solution_two():
    input_list = parse_input('input.txt')
    count = 0
    for i in range(3, len(input_list)):
        count += (input_list[i - 3] < input_list[i])
    return count


if __name__ == '__main__':
    print( f"The solution to question one is: {solution_one()}")
    print( f"The solution to question two is: {solution_two()}")
