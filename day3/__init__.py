def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]
        return input_list


def solution_one():
    input_list = parse_input('input.txt')
    m_num = 0
    l_num = 0

    for i in range(len(input_list[0])):
        count_one = 0
        count_zero = 0
        for j in range(len(input_list)):
            count_one += (input_list[j][i] == '1')
            count_zero += (input_list[j][i] == '0')

        if count_one > count_zero:
            m_num = m_num * 2 + 1
            l_num *= 2
        else:
            l_num = l_num * 2 + 1
            m_num *= 2

    return l_num * m_num


def filer_nums(input_list, greater=True):
    i = 1
    while len(input_list) != 1:
        z = []
        o = []
        for num in input_list:
            if num[i] == '1':
                o.append(num)
            else:
                z.append(num)
        i += 1
        if greater:
            input_list = o if len(o) >= len(z) else z
        else:
            input_list = z if len(o) >= len(z) else o

    return input_list


def solution_two():
    input_list = parse_input('input.txt')
    zero_leading = []
    one_leading = []

    for num in input_list:
        if num[0] == '1':
            one_leading.append(num)
        else:
            zero_leading.append(num)

    m_c = one_leading if len(one_leading) >= len(zero_leading) else zero_leading
    l_c = zero_leading if len(one_leading) >= len(zero_leading) else one_leading

    return int(filer_nums(m_c)[0], 2) * int(filer_nums(l_c, False)[0], 2)


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
