import queue


def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1].split('-') for i in input_list]
        paths = {}
        for pair in input_list:
            if pair[0] in paths:
                paths[pair[0]] = paths[pair[0]] + [pair[1]]
            else:
                paths[pair[0]] = [pair[1]]

            if pair[1] in paths:
                paths[pair[1]] = paths[pair[1]] + [pair[0]]
            else:
                paths[pair[1]] = [pair[0]]
        return paths


def solution_one():
    paths = parse_input('input.txt')
    # Construct all the paths making sure we never path thru a small cave twice
    possible_paths = [['start']]
    valid_paths = []
    while len(possible_paths) != 0:
        temp = []
        while len(possible_paths) != 0:
            # Construct the possible paths from the partial path
            cur = possible_paths.pop(0)
            for neighbour in paths[cur[-1]]:
                if neighbour == 'end':  # Check if neighbour is end in that case append to valid paths
                    valid_paths.append(cur + [neighbour])
                elif neighbour.isupper() or neighbour not in cur:  # Check if neighbour is already visited and a small cave
                    temp.append(cur + [neighbour])
        possible_paths = temp

    print(valid_paths)
    return len(valid_paths)


def solution_two():
    paths = parse_input('input.txt')
    # Construct all the paths making sure we know if we already passed thru a small cave once
    possible_paths = [[0, 'start']]
    valid_paths = []
    while len(possible_paths) != 0:
        temp = []
        while len(possible_paths) != 0:
            # Construct the possible paths from the partial path
            cur = possible_paths.pop(0)
            for neighbour in paths[cur[-1]]:
                if neighbour == 'end':  # Check if neighbour is end in that case append to valid paths
                    valid_paths.append(cur + [neighbour])
                elif neighbour.isupper() or neighbour not in cur:  # Check if neighbour is already visited and a small cave
                    temp.append(cur + [neighbour])
                elif neighbour in cur and neighbour != "start" and cur[0] == 0:
                    temp.append([1] + cur[1:] + [neighbour])
        possible_paths = temp

    print(valid_paths)
    return len(valid_paths)


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
