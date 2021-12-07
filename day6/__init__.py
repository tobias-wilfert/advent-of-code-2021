def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = input_list[0][:-1].split(',')
        input_list = [int(i) for i in input_list]
        return input_list


def solution_one(n=80):
    input_list = parse_input('input.txt')
    age = {}
    for i in input_list:
        age[i] = 1 if i not in age else age[i] + 1

    for t in range(n):
        temp = {}
        for k, v in age.items():
            if k == 0:
                temp[8] = v + temp[8] if 8 in temp else v
                temp[6] = v + temp[6] if 6 in temp else v
            else:
                temp[k-1] = v + temp[k-1] if k-1 in temp else v
        age = temp

    count = 0
    for k, v in age.items():
        count += v
    return count


def solution_two():
    return solution_one(256)


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
