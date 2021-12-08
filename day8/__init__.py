def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1].split(' | ') for i in input_list]
        input_list = [[i[0].split(' '), i[1].split(' ')] for i in input_list]
        return input_list


def solution_one():
    input_list = parse_input('input.txt')
    count = 0
    for line in input_list:
        for signal in line[1]:
            if len(signal) in (2, 4, 3, 7):
                count += 1
    return count


def solution_two():
    input_list = parse_input('input.txt')
    count = 0

    for line in input_list:
        m = {}
        line[0].sort(key=lambda x: len(x))
        inputs = ["".join(sorted(i)) for i in line[0]]
        one = inputs[0]
        four = inputs[2]
        # Easy ones
        m[inputs[0]] = '1'
        m[inputs[1]] = '7'
        m[inputs[2]] = '4'
        m[inputs[-1]] = '8'
        len_five = [i for i in inputs if len(i) == 5]  # 2,3,5
        len_six = [i for i in inputs if len(i) == 6]  # 0,9,6

        # Identify 2,3,5
        three = [i for i in len_five if len(set(one)-set(i)) == 0][0]  # 1-3 = 0
        len_five.remove(three)
        m[three] = '3'
        five = [i for i in len_five if len(set(i)-set(four)) == 2][0]  # 5-4 = 2
        len_five.remove(five)
        m[five] = '5'
        two = len_five[0]
        m[two] = '2'

        # Identify 0,6,9
        six = [i for i in len_six if len(set(one) - set(i)) == 1][0]  # 1-6 = 1
        len_six.remove(six)
        m[six] = '6'
        nine = [i for i in len_six if len(set(i) - set(four)) == 2][0]  # 9-4 = 2
        len_six.remove(nine)
        m[nine] = '9'
        zero = len_six[0]
        m[zero] = '0'

        # Find the output number:
        # Map the sorted string to the number(string) join the strings and convert to int—
        count += int("".join([m["".join(sorted(i))] for i in line[1]]))

    return count


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
