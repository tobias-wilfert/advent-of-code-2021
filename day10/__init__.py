def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]
        return input_list


def solution_one():
    maping = {'[': ']',
              '(': ')',
              '{': '}',
              '<': '>'}
    score = {')': 3, ']':57, '}':1197, '>': 25137}
    count = 0
    input_list = parse_input('input.txt')
    # Use a stack loop over the string push and pop, if we find a collision on the stack the line is corrupted
    for line in input_list:
        stack = []
        for char in line:
            if char in "[({<":
                stack.append(char)
            else:
                # Check if the correct thing is on the stack
                if len(stack) == 0:
                    break
                if maping[stack.pop()] != char:
                    count += score[char]

    return count


def solution_two():
    maping = {'[': ']',
              '(': ')',
              '{': '}',
              '<': '>'}
    score = {'(': 1, '[':2, '{':3, '<':4}
    counts = []
    input_list = parse_input('input.txt')

    for line in input_list:
        stack = []
        c = False
        count = 0
        for char in line:
            if char in "[({<":
                stack.append(char)
            else:
                if maping[stack.pop()] != char:
                    c = True
                    break
        if not c:
            while len(stack):
                count = count*5 + score[stack.pop()]
            counts.append(count)

    counts.sort()
    return counts[int(len(counts)/2)]


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
