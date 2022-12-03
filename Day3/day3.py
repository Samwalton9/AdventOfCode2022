from helpers import load_input_as_lines


def find_unique_character(*lists) -> str:
    common_elements = list(set.intersection(*map(set, [*lists])))

    # There's only one
    return common_elements[0]


def convert_to_priority(character: str) -> int:
    # ord() is 65-90 for A-Z and 97-122 for a-z
    ord_value = ord(character)
    if ord_value >= 97:
        return ord_value - 96
    else:
        return ord_value - 65 + 27


def day_1():
    priority_sum = 0
    for line in load_input_as_lines():
        line_length = len(line)
        half_length = line_length//2
        unique_char = find_unique_character(line[:half_length], line[half_length:])

        priority_sum += convert_to_priority(unique_char)

    print(priority_sum)


def day_2():
    priority_sum = 0
    input_lines = load_input_as_lines()

    step = 0
    for i in range(len(input_lines)//3):
        group = input_lines[step:step+3]
        print(i, step, group)
        unique_char = find_unique_character(*group)

        priority_sum += convert_to_priority(unique_char)
        step += 3

    print(priority_sum)


day_2()
