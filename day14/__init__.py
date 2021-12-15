def parse_input(file_name):
    with open(file_name, 'r') as input_file:
        # Get the input_list
        input_list = input_file.readlines()
        # Remove the newline at the end of each line
        input_list = [i[:-1] for i in input_list]

        # Split up in dots and fold instructions
        # Parse the split instructions
        sequence = ""
        replacements = {}
        seen_newline = False
        for line in input_list:
            if not line:
                seen_newline = True
            elif not seen_newline:
                sequence = line
            else:
                temp = line.split(' -> ')
                replacements[temp[0]] = temp[1]
        return sequence, replacements


def solution_one():
    sequence, replacements = parse_input('test.txt')

    # Do the insertion rules x times
    for i in range(10):
        new_sequence = ""
        for p in range(len(sequence)-1):
            # Find the item that will newly be inserted
            insert = replacements[sequence[p:p+2]] if sequence[p:p+2] in replacements else ''
            new_sequence += (sequence[p] + insert)

        new_sequence += sequence[-1]  # Add the trailing character
        sequence = new_sequence

    # Get the frequency of the characters
    frequency = {}
    for char in sequence:
        frequency[char] = 1 if char not in frequency else frequency[char] + 1

    # Find the min and max element
    minF = frequency[min(frequency, key=lambda x: frequency[x])]
    maxF = frequency[max(frequency, key=lambda x: frequency[x])]
    return maxF - minF


def solution_two():
    sequence, replacements = parse_input('input.txt')
    pair_frequency = {}
    char_frequency = {}

    # Loop over the initial characters
    for p in range(len(sequence) - 1):
        char = sequence[p]
        pair = sequence[p:p + 2]
        char_frequency[char] = char_frequency[char] + 1 if char in char_frequency else 1
        pair_frequency[pair] = pair_frequency[pair] + 1 if pair in pair_frequency else 1
    # Add the final char
    char_frequency[sequence[-1]] = char_frequency[sequence[-1]] + 1 if sequence[-1] in char_frequency else 1

    # Do the insertions x times
    for i in range(40):
        # Pairs will be altered by insertion
        new_frequency = {}
        # Loop over the existing pairs
        for key, value in pair_frequency.items():
            # Find the insertion item if it exists
            inter = replacements[key] if key in replacements else ''
            if inter != '':
                char_frequency[inter] = value if inter not in char_frequency else char_frequency[inter] + value
                pairs = [key[0] + inter, inter + key[1]]
                for pair in pairs:
                    new_frequency[pair] = value if pair not in new_frequency else new_frequency[pair] + value
            else:
                new_frequency[key] = value

        pair_frequency = new_frequency

    # Find the min and max element
    minF = char_frequency[min(char_frequency, key=lambda x: char_frequency[x])]
    maxF = char_frequency[max(char_frequency, key=lambda x: char_frequency[x])]
    return maxF - minF


if __name__ == '__main__':
    print(f"The solution to question one is: {solution_one()}")
    print(f"The solution to question two is: {solution_two()}")
